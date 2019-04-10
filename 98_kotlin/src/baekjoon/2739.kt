//https://www.acmicpc.net/problem/2739
//구구단


package baekjoon

import java.io.*

fun main(args:Array<String>){
    val s = BufferedReader(InputStreamReader(System.`in`)).readLine()
    val a = Integer.parseInt(s)
    val sb = StringBuffer()
    for (n in 1..9) {
        sb.append("$a * $n = ${a * n}\n")
    }
    println(sb.toString())
}