//https://www.acmicpc.net/problem/10869
//사칙연산


package baekjoon

import java.io.*

fun main(args:Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val s = br.readLine().split(" ")
    val a = Integer.parseInt(s[0])
    val b = Integer.parseInt(s[1])
    val sb = StringBuffer()
    sb.append("${a + b}\n").append("${a - b}\n").append("${a * b}\n").append("${a / b}\n").append("${a % b}\n")
    println(sb.toString())
}