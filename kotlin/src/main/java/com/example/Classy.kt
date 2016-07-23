package com.example

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

// Tokens

//enum class Token {
//    NUMBER, COMMAND, EOF, ID
//}

val READ_TOKENS = mutableListOf(Token(Type.BOF, null), Token(Type.EOL, null))

val SYMBOLS = hashSetOf(Symbol("lol", 696969))

data class Token(val type: Type, val value: Any?)

data class Symbol(val id: String, val value: Any?)

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
                println(currentChar)
            }
            println()
            currentLine = input.readLine()
        }
    } catch(e: FileNotFoundException) {
        println("File not found")
        return
    } catch(e2: IOException) {
        println("IOException")
    } finally {
        input?.close()
    }
}

fun switchState(input: Char) : Boolean {
    if (state == State.EMPTY) {

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
    } else if (state == State.RARM3 && input == '2') {
        state = State.LARM2
        return true
    }
    return false
}