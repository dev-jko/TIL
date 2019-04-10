//https://www.acmicpc.net/problem/2438
//별 찍기 - 1


package baekjoon

import java.io.*

fun main() {
    val n = Integer.parseInt(BufferedReader(InputStreamReader(System.`in`)).readLine())
    val sb = StringBuffer()
    var line = ""
    for (a in 1..n) {
        line += "*"
        sb.append("$line\n")
    }
    println(sb.toString())
}