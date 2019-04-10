// https://www.acmicpc.net/problem/2439
// 별 찍기 - 2


package baekjoon

import java.io.*

fun main(args:Array<String>) {
    val n = Integer.parseInt(BufferedReader(InputStreamReader(System.`in`)).readLine())
    val sb = StringBuffer()
    for (i in 1..n) {
        for (j in 1..(n-i)) sb.append(" ")
        for (j in 1..i) sb.append("*")
        sb.append("\n")
    }
    println(sb.toString())
}