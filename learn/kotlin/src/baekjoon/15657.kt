//  https://www.acmicpc.net/problem/15657
//  N과 M (8)


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val arr = br.readLine().split(" ").map { it.toInt() }.sorted()
    val selected = Array(M) { 0 }
    val sb = StringBuffer()
    sequence(0, M, selected, arr, sb)
    println(sb.toString())
}

fun sequence(k: Int, n: Int, selected: Array<Int>, arr: List<Int>, sb: StringBuffer) {
    if (k == n) {
        sb.append("${selected.joinToString(separator = " ", transform = { arr[it].toString() })}\n")
    } else {
        for (i in (if (k == 0) 0 else selected[k - 1]) until arr.size) {
            selected[k] = i
            sequence(k + 1, n, selected, arr, sb)
        }
    }
}
