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
    val result = HashSet<String>()
    val sb = StringBuffer()
    sequence15663(0, M, selected, arr, result, sb)
    println(sb.toString())
}

fun sequence15663(k: Int, n: Int, selected: Array<Int>, arr: List<Int>, result: HashSet<String>, sb: StringBuffer) {
    if (k == n) {
        val key = selected.joinToString(separator = " ", transform = { arr[it].toString() })
        if (result.contains(key)) return
        result.add(key)
        sb.append(key + "\n")
    } else {
        for (i in 0 until arr.size) {
            if (i in selected) continue
            selected[k] = i
            sequence15663(k + 1, n, selected, arr, result, sb)
            selected[k] = -1
        }
    }
}
