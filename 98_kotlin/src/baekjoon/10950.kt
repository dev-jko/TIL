//https://www.acmicpc.net/problem/10950
//A+B - 3


package baekjoon

import java.io.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = Integer.parseInt(br.readLine())
    val sb = StringBuffer()
    for (i in 1..n) {
        val s = br.readLine().split(" ")
        val a = Integer.parseInt(s[0])
        val b = Integer.parseInt(s[1])
        sb.append("${a + b}\n")
    }
    println(sb.toString())
}