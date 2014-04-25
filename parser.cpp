#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int parenthesis_check(string s) {
	if (s == "")
		return -1;
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == '(') {
			return i;
		}
	}
	return -1;
}

int par_2check(string s) {
	if (s == "")
		return -1;
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == ')') {
			return i;
		}
	}
	return -1;
}

int comma_pos_check(string s) {
	if (s == "")
		return -1;
	// goes backwards for speed
	for (int i = s.length() - 1; i > 0; --i) {
		if (s[i] == ',') {
			return i;
		}
	}
	return -1;
}

//string def_pos_check(string s, string& def2) {
//	// if there is a pos in the middle of the line, 
//	// then this will return it and the definition that was before it
//	if (s == "")
//		return false;
//	for (int i = 0; i < s.length(); ++i) {
//		if (s[i] == '.') {
//			int j = i;
//			if (s[i + 1] == ')' || s[i + 1] == ']') {
//				break;
//			}
//			else {
//				while (s[j] != ' ') {
//					j--;
//				}
//			}
//			// this variable will be the place holder for the index of the 
//			// definition up to the space before the pos
//			// used in the for loop below
//			int m = j;
//			string pos;
//			while (j < i) {
//				pos += s[++j];
//			}
//			for (int n = 0; n < m; ++n) {
//				def2 += s[n];
//			}
//			return pos;
//		}
//	}
//	return "";
//}

bool pos_check(string& s) {
	if (s == "")
		return false;
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == '.' && s[i + 1] != ')' && s[i + 1] != ']') {
			int ind = comma_pos_check(s);
			if (ind != -1) {
				s.erase(ind, 1);
			}
			return true;
		}
	}
	return false;
}

void commas(ifstream& in, ofstream& out) {

	while (1) {
		string line;
		getline(in, line);
		if (line == "THIS_IS_THE_END") break;
		if (line == "") continue;
		if (line[line.length() - 1] != ',')
			out << line << "," << endl;
		else out << line << endl;
	}
}

int comma_count(stringstream& ss) {
	string s;
	ss >> s;
	int count = 0;
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == ',') {
			count++;
		}
	}
	return count;
}

/*string switch_quotes(string s) {
	// switches all double quotes inside of definitions to single quotes
	if (s == "")
		return "";
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == '\"'){
			s[i] = '\'';
		}
	}
	return s;
}*/

string engword(ifstream& in) {
	string word, def, line;
	stringstream ss;
	getline(in, line);
	// used as a end of file flag
	if (line == "THIS_IS_THE_END") {
		return "";
	}

	ss << line;
	int num = 0;
	while (1) {
		//cout << ++num;
		ss >> word;
		int p = parenthesis_check(word);
		if (word == "") break;
		if (p > -1) {
			word.erase(p, word.length() - 1);
			if (def == "")
			{
				def += word;
				break;
			}
			else {
				def += " " + word;
				break;
			}
		}
		else if (def == "")
		{
			def += word;
		}
		else def += " " + word;
		if (!ss.good()) break;
	}
	return def;
}

void pos_body(string& pos, string def, vector<string> defs, string line, string eng, ofstream& out) {
	stringstream ss;
	string s;
	ss << line;

	//ss >> s;
	// get the pos if there is one
	int Opar = parenthesis_check(line);
	if (Opar != -1) {
		int Cpar = par_2check(line);
		string str;
		str += line.substr(Opar, Cpar);

		if (!pos_check(pos))
			out << "\"" << eng << "\",\"" << str << "\"," << endl;
		else
			out << "\"" << eng << "\",\"" << str << "\",\"" << pos << "\"" << endl;

	}
	else {
		ss >> pos;
		if (!pos_check(pos)) {

			if (pos[pos.length() - 1] == ',') {
				pos.erase(pos.length() - 1, 1);
				def = pos;
				defs.push_back(def);
				pos = "";
			}
			else {
				getline(ss, line, ',');
				def += pos + line;
				defs.push_back(def);
				pos = "";
			}
		}
		// way to keep the part of speech for the lines that contain only something in parenthesis
		//else { pos = s; }

		// split up definitions that are split up by a ,
		while (getline(ss, def, ',')) {
			if (def[0] == ' ') {
				// get rid of the spaces before definitions
				def.erase(0, 1);
			}
			defs.push_back(def);
		}

		for (int i = 0; i < defs.size(); ++i) {
			out << eng << "\t" << "\"" << defs[i] << "\"" << "\t" << pos << endl;
		}

	}
}

bool POS_get(ifstream& in, ifstream& in2, ofstream& out) {
	// one line at a time
	string def, line, line2, pos;
	vector<string> defs;
	getline(in, line);
	if (line == "THIS_IS_THE_END") {
		return false;
	}

	// get the word in english
	string eng = engword(in2);


	//line = switch_quotes(line);
	pos_body(pos, def, defs, line, eng, out);

	char c;
	while (1) {
		c = in.get();
		if (c == '2') {
			getline(in, line2);
			line.erase(0, 2);
			pos_body(pos, def, defs, line2, eng, out);
		}
		else {
			in.unget();
			break;
		}
	}

	return true;
}



int main() {
	ifstream in;
	in.open("swedish2.txt");
	ofstream out;
	out.open("English-SwedishTEST.txt");
	ifstream in2;
	in2.open("words.txt");


	if (!in.good()) return 0;
	if (!in2.good()) return 0;

	
	bool good = true;
	while (good) {
		good = POS_get(in, in2, out);
	}

	in2.close();
	in.close();
	out.close();
}