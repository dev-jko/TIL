//  https://www.acmicpc.net/problem/15656
//  N과 M (7)


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val arr = br.readLine().split(" ").map { it.toInt() }.sorted()
    val selected = Array(M) { 0 }
    val sb = StringBuffer()
    perm15656(0, M, selected, arr, sb)
    println(sb.toString())
}

fun perm15656(k: Int, n: Int, selected: Array<Int>, arr: List<Int>, sb: StringBuffer) {
    if (k == n) {
        sb.append("${selected.joinToString(separator = " ", transform = { arr[it].toString() })}\n")
    } else {
        for (i in 0 until arr.size) {
            selected[k] = i
            perm15656(k + 1, n, selected, arr, sb)
        }
    }
}