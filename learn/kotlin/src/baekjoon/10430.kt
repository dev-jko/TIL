//https://www.acmicpc.net/problem/10430
//나머지


package baekjoon


import java.io.*

fun main(args: Array<String>) {
    val s = BufferedReader(InputStreamReader(System.`in`)).readLine().split(" ")
    val A = Integer.parseInt(s[0])
    val B = Integer.parseInt(s[1])
    val C = Integer.parseInt(s[2])
    val sb = StringBuffer()
    sb.append("${(A + B) % C}\n").append("${(A % C + B % C) % C}\n").append("${(A * B) % C}\n").append("${(A % C * B % C) % C}\n")
    println(sb.toString())
}