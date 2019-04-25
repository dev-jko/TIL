//  https://www.acmicpc.net/problem/15663
//  N과 M (9)


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val arr = br.readLine().split(" ").map { it.toInt() }.sorted()
    val selected = Array(M) { -1 }
    val sb = StringBuffer()
    sequence15663(0, M, selected, arr, sb)
    println(sb.toString())
}

fun sequence15663(k: Int, n: Int, selected: Array<Int>, arr: List<Int>, sb: StringBuffer) {
    if (k == n) {
        sb.append("${selected.joinToString(separator = " ", transform = { arr[it].toString() })}\n")
    } else {
        var before = 0
        for (i in 0 until arr.size) {
            if (arr[i] == before || i in selected) continue
            selected[k] = i
            before = arr[i]
            sequence15663(k + 1, n, selected, arr, sb)
            selected[k] = -1
        }
    }
}
