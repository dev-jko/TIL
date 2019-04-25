//  https://www.acmicpc.net/problem/2448
//  별 찍기 - 11


package baekjoon

import java.io.*
import kotlin.math.log2

fun main(args: Array<String>) {
    val n = log2(Integer.parseInt(BufferedReader(InputStreamReader(System.`in`)).readLine()).toFloat() / 3).toInt()
    val sb = StringBuffer()
    val arr = arrayListOf("  *  ", " * * ", "*****")
    for (i in 1..n) {
        star(arr)
    }
    for (i in 0 until arr.size) {
        sb.append("${arr[i]}\n")
    }
    println(sb.toString())
}

fun star(arr: ArrayList<String>) {
    val len = arr.size
    for (i in 0 until len) {
        arr.add("${arr[i]} ${arr[i]}")
    }
    val temp = " ".repeat(len)
    for (i in 0 until len) {
        arr[i] = "$temp${arr[i]}$temp"
    }
}