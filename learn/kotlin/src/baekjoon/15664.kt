//  https://www.acmicpc.net/problem/15664
//  N과 M (10)


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val arr = br.readLine().split(" ").map { it.toInt() }.sorted()
    val selected = Array(M) { -1 }
    val used = Array(N) { false }
    val sb = StringBuffer()
    sequence15664(0, M, selected, used, arr, sb)
    println(sb.toString())
}

fun sequence15664(k: Int, n: Int, selected: Array<Int>, used: Array<Boolean>, arr: List<Int>, sb: StringBuffer) {
    if (k == n) {
        sb.append("${selected.joinToString(separator = " ", transform = { arr[it].toString() })}\n")
    } else {
        var before = -1
        for (i in (if (k == 0) 0 else selected[k - 1] + 1) until arr.size) {
            if (arr[i] == before || used[i]) continue
            selected[k] = i
            used[i] = true
            before = arr[i]
            sequence15664(k + 1, n, selected, used, arr, sb)
            used[i] = false
        }
    }
}
