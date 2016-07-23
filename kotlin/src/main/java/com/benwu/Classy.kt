package com.benwu

import java.io.BufferedReader
import java.io.FileNotFoundException
import java.io.FileReader
import java.io.IOException
import java.util.*

/**
 * Created by Ben Wu on 2016-06-03.
 */

/**
 *    ¯\_(ツ)_/¯
 */

val READ_TOKENS = mutableListOf(Token(Type.BOF, null), Token(Type.EOL, null))
val TOKEN_LINES = mutableListOf(mutableListOf(Token(Type.BOF, null)))

val initializalization: Any? = 696969

val SYMBOLS = hashMapOf(Pair("lol", initializalization))

var currentSymbol = StringBuilder() // characters in the current id
var lastSymbol = ""
var currentValue = StringBuilder() // characters in the current val

data class Token(val type: Type, val value: Any?)

data class Symbol(val id: String, val value: Any?) {
    override fun equals(other: Any?): Boolean {
        return other is Symbol && other.id == id
    }

    override fun hashCode(): Int {
        return super.hashCode()
    }
}

enum class Type {
    STRING, NUMBER, ID, SHRUG, BOF, EOF, EOL
}

// Input states

enum class State {
    EMPTY, LARM1, LARM2, LARM3, FACE1, FACE2, FACE3, RARM1, RARM2, RARM3, VAL, ID
}

val LARM1 = '¯'
val LARM2 = '\\'
val LARM3 = '_'
val FACE1 = '('
val FACE2 = 'ツ'
val FACE3 = ')'
val RARM1 = '_'
val RARM2 = '/'
val RARM3 = '¯'

var state = State.EMPTY

fun main(args: Array<String>) {
    val testing = true

    var lineNumber = 1

    var input: BufferedReader? = null

    // read lines from file
    try {
        input = BufferedReader(FileReader(
                if(!testing)
                    readLine()
                else
                    """C:\Users\bw964\Desktop\testinput.txt"""))

        var currentLine: String? = input.readLine();
        while(currentLine != null) {
            println(currentLine)

            for(currentChar in currentLine.iterator()) {
                if(!switchState(currentChar)) {
                    throw Exception("Syntax error on line $lineNumber with character: $currentChar")
                }
            }
            if (state == State.VAL) {
                READ_TOKENS.add(Token(Type.NUMBER, currentValue.toString().toDouble()))
            } else if (state == State.ID) {
                READ_TOKENS.add(Token(Type.ID, currentSymbol.toString()))
            }
            READ_TOKENS.add(Token(Type.EOL, null))
            state = State.EMPTY
            currentLine = input.readLine()
            ++lineNumber
        }
        READ_TOKENS.add(Token(Type.EOF, null))

        createSymbols()
    } catch(e: FileNotFoundException) {
        println("File not found")
        return
    } catch(e2: IOException) {
        println("IOException")
        return
    } catch (e3: Exception) {
        println(e3.message)
        return
    } finally {
        input?.close()
    }

    println("fam")
}

// tokenizer
fun switchState(input: Char) : Boolean {
    if(input == ' ' || input == '\t' || input == '\n') {
        return true
    }
    if (state == State.EMPTY) {
        if (input in 'a'..'z' || input in 'A'..'Z') {
            state = State.ID
            currentSymbol = StringBuilder()
            currentSymbol.append(input)
            return true
        } else if (input == LARM1) {
            state = State.LARM1
            return true
        } else if (input in '0'..'9') {
            state = State.VAL
            currentValue = StringBuilder()
            currentValue.append(input)
            return true
        }
    } else if (state == State.ID) {
        if (input in 'a'..'z' || input in 'A'..'Z') {
            state = State.ID
            currentSymbol.append(input)
            return true
        } else if (input == LARM1) {
            state = State.LARM1
            lastSymbol = currentSymbol.toString()
            READ_TOKENS.add(Token(Type.ID, lastSymbol))
            return true
        } else if (input in '0'..'9') {
            state = State.VAL
            lastSymbol = currentSymbol.toString()
            currentValue = StringBuilder()
            currentValue.append(input)
            READ_TOKENS.add(Token(Type.ID, lastSymbol))
            return true
        }
    } else if (state == State.VAL) {
        if (input == LARM1) {
            state = State.LARM1
            READ_TOKENS.add(Token(Type.NUMBER, currentValue.toString().toDouble()))
            return true
        } else if (input in '0'..'9') {
            state = State.VAL
            currentValue.append(input)
            return true
        }
    } else if (state == State.LARM1 && input == LARM2) {
        state = State.LARM2
        return true
    } else if (state == State.LARM2 && input == LARM3) {
        state = State.LARM3
        return true
    } else if (state == State.LARM3 && input == FACE1) {
        state = State.FACE1
        return true
    } else if (state == State.FACE1 && input == FACE2) {
        state = State.FACE2
        return true
    } else if (state == State.FACE2 && input == FACE3) {
        state = State.FACE3
        return true
    } else if (state == State.FACE3 && input == RARM1) {
        state = State.RARM1
        return true
    } else if (state == State.RARM1 && input == RARM2) {
        state = State.RARM2
        return true
    } else if (state == State.RARM2 && input == RARM3) {
        state = State.EMPTY
        READ_TOKENS.add(Token(Type.SHRUG, null))
        return true
    }
    return false
}

// symbolizer and separating tokens by line
fun createSymbols() {
    val currentLineTokens = mutableListOf(Token(Type.BOF, null))
    for(currentToken in READ_TOKENS) {
        if(currentToken.type == Type.EOL) {
            TOKEN_LINES.add(ArrayList(currentLineTokens))
            if (currentLineTokens.size in 2..3 && currentLineTokens[0].type == Type.SHRUG && currentLineTokens[1].type == Type.ID) {
                val success: Any? = if (currentLineTokens.size == 2) {
                    SYMBOLS.put(currentLineTokens[1].value.toString(), null)
                } else if (currentLineTokens[2].type == Type.NUMBER) {
                    SYMBOLS.put(currentLineTokens[1].value.toString(), currentLineTokens[2].value) // TODO: can re-define unintialized variables
                } else {
                    return
                }
                if (success != null) {
                    throw Exception("Symbol ${currentLineTokens[1].value.toString()} already exists")
                }
            }
            currentLineTokens.clear()
        } else {
            currentLineTokens.add(currentToken)
        }
    }
}