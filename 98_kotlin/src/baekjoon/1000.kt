package baekjoon

import java.io.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val s = br.readLine().split(" ")
    val a = Integer.parseInt(s[0])
    val b = Integer.parseInt(s[1])
    println(a + b)
}