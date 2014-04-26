package edu.byu.arclite.dictionary.loaders

import java.io.File
import java.util.Date
import edu.byu.arclite.dictionary.Dictionary

/**
 * This handles all the creation of dictionaries based on the dictionaries Giovanni supplied
 * Date: 2/5/2013
 * @author Josh Monson
 */
object GiovanniDictionaryCreator {

  // List of dictionaries to load
  val giovanniDictionaries = List(
    "englishToPortuguese"
    /*"englishToKorean",
    "englishToJapanese",
    "englishToFrench",
    "englishToGerman",
    "englishToItalian",
    "englishToSpanish",
    "englishToDutch",
	"englishToRussian",
    "englishToChinese"*/
    //"englishToRussian"
  )

  // URIs of the text files
  val giovanniDictionaryTextFiles = Map(
    "englishToFrench" -> "src/main/resources/English-French.txt",
    "englishToGerman" -> "src/main/resources/English-German.txt",
    "englishToItalian" -> "src/main/resources/English-Italian.txt",
    "englishToSpanish" -> "src/main/resources/English-Spanish.txt",
    "englishToDutch" -> "src/main/resources/English-Dutch.txt",
    "englishToRussian" -> "src/main/resources/English-Russian.txt",
    "englishToPortuguese" -> "src/main/resources/English-Portuguese.txt",
    "englishToChinese" -> "src/main/resources/English-Chinese(T).txt",
    "englishToKorean" -> "src/main/resources/English-Korean.txt",
    "englishToJapanese" -> "src/main/resources/English-Japanese.txt"
  )

  // URIs of the finished dictionary files
  val giovanniDictionaryFiles = Map(
    "englishToFrench" -> "src/main/resources/en-fr.bin",
    "englishToGerman" -> "src/main/resources/en-de.bin",
    "englishToItalian" -> "src/main/resources/en-it.bin",
    "englishToSpanish" -> "src/main/resources/en-es.bin",
    "englishToDutch" -> "src/main/resources/en-nl.bin",
    "englishToRussian" -> "src/main/resources/en-ru.bin",
    "englishToPortuguese" -> "src/main/resources/en-pt.bin",
    "englishToChinese" -> "src/main/resources/en-zh.bin",
    "englishToKorean" -> "src/main/resources/en-ko.bin",
    "englishToJapanese" -> "src/main/resources/en-ja.bin"
  )

  // URIs of the reverse dictionary files
  val giovanniReverseDictionaryFiles = Map(
    "englishToFrench" -> "src/main/resources/fr-en.bin",
    "englishToGerman" -> "src/main/resources/de-en.bin",
    "englishToItalian" -> "src/main/resources/it-en.bin",
    "englishToSpanish" -> "src/main/resources/es-en.bin",
    "englishToDutch" -> "src/main/resources/nl-en.bin",
    "englishToRussian" -> "src/main/resources/ru-en.bin",
    "englishToPortuguese" -> "src/main/resources/pt-en.bin",
    "englishToChinese" -> "src/main/resources/zh-en.bin",
    "englishToKorean" -> "src/main/resources/ko-en.bin",
    "englishToJapanese" -> "src/main/resources/ja-en.bin"
  )
  
    val partsOfSpeech = Map(
    "englishToFrench" -> List("bloop", "blap", "bleep"),
    "englishToGerman" -> List("bloop", "blap", "bleep"),
    "englishToItalian" -> List("bloop", "blap", "bleep"),
    "englishToSpanish" -> List("bloop", "blap", "bleep"),
    "englishToDutch" -> List("bloop", "blap", "bleep"),
    "englishToRussian" -> List("bloop", "blap", "bleep"),
    "englishToPortuguese" -> List("bloop", "blap", "bleep"),
    "englishToChinese" -> List("bloop", "blap", "bleep"),
    "englishToKorean" -> List("bloop", "blap", "bleep"),
    "englishToJapanese" -> List("bloop", "blap", "bleep")
  )
  

  /**
   * This creates a dictionary based on the name
   * @param dictionaryName The name of the dictionary to create
   */
  def createDictionary(dictionaryName: String) {
    // Keep track of time
    val start = new Date().getTime

    // Create the dictionary loader
    val dictionaryTextFile = new File(giovanniDictionaryTextFiles(dictionaryName))
    val loader = new GiovanniDictionaryLoader(dictionaryTextFile)

    // Create the dictionary and save it to file
    val dictionary = Dictionary.createDictionary(loader)
    val dictionaryFile = new File(giovanniDictionaryFiles(dictionaryName))
    Dictionary.saveToFile(dictionary, dictionaryFile)

    // How long did it take?
    val end = new Date().getTime
    println("Dictionary \"" + dictionaryName + "\" created in " + (end - start) + " ms.")
  }

  /**
   * This creates a reverse dictionary based on the name
   * @param dictionaryName The name of the dictionary to create
   */
  def createReverseDictionary(dictionaryName: String) {
    // Keep track of time
    val start = new Date().getTime

    // Create the dictionary loader
    val dictionaryTextFile = new File(giovanniDictionaryTextFiles(dictionaryName))
    val loader = new GiovanniReverseDictionaryLoader(dictionaryTextFile)

    // Create the dictionary and save it to file
    val dictionary = Dictionary.createDictionary(loader)
    val dictionaryFile = new File(giovanniReverseDictionaryFiles(dictionaryName))
    Dictionary.saveToFile(dictionary, dictionaryFile)

    // How long did it take?
    val end = new Date().getTime
    println("Reverse dictionary \"" + dictionaryName + "\" created in " + (end - start) + " ms.")
  }

  /**
   * This creates all the dictionaries
   */
  def createDictionaries() {
    println("Loading Giovanni's dictionaries...")
    for (dictionaryName <- giovanniDictionaries) {
      createDictionary(dictionaryName)
      createReverseDictionary(dictionaryName)
    }
  }

  def test(dictionaryName: String, keys: List[String]) {

    val dictionaryFileName =
      if (dictionaryName.substring(0,2) == "R_")
        giovanniReverseDictionaryFiles(dictionaryName.substring(2))
      else
        giovanniDictionaryFiles(dictionaryName)

    val dictionaryFile = new File(dictionaryFileName)
    val dictionary = Dictionary.loadFromFile(dictionaryFile)
    for (key <- keys) {
      println("Dictionary entry for \"" + key + "\":")
      println(dictionary(key))
    }

  }
  
  def formatDictionaries() {
	for (dictionaryName <- giovanniDictionaries) {
	  for(bl <- partsOfSpeech(dictionaryName)) {
		println(bl)
	  }
	}
  }

}
