//  https://www.acmicpc.net/problem/11721
//  열 개씩 끊어 출력하기


package baekjoon


import java.io.*

fun main() {
    val s = BufferedReader(InputStreamReader(System.`in`)).readLine()
    val sb = StringBuffer()
    for (i in 0 until s.length step 10) {
        if (i + 10 < s.length) sb.append("${s.substring(i, i + 10)}\n")
        else sb.append("${s.substring(i)}\n")
    }
    println(sb.toString())
}