// https://www.acmicpc.net/problem/2443
// 별 찍기 - 6


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args: Array<String>) {
    val N = BufferedReader(InputStreamReader(System.`in`)).readLine().toInt()
    val n = N * 2
    val sb = StringBuffer()
    for (i in 0 until N) {
        sb.append("${" ".repeat(i)}${"*".repeat(n - (i * 2 + 1))}\n")
    }
    print(sb.toString())
}