//  https://www.acmicpc.net/problem/1107
//  리모컨

package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N = Integer.parseInt(br.readLine())
    val n = Integer.parseInt(br.readLine())
    val memo = Array<Int>(1000001) { -1 }
    val input = if (n > 0) br.readLine().split(" ") else listOf()
    val inputs: List<Char> = input.map { it[0] }
    for (i in 0..3) {
        memo[100 + i] = i
        memo[100 - i] = i
    }
    for (i in 0..1000000) {
        val temp = i.toString().toCharArray()
        var check = true
        for (s in temp) {
            if (s in inputs) {
                check = false
                break
            }
        }
        if (check) {
            when {
                memo[i] == -1 -> {
                    memo[i] = temp.size
                }
                memo[i] > temp.size -> {
                    memo[i] = temp.size
                }
            }
        } else if (i > 0 && memo[i - 1] != -1 && (memo[i] == -1 || (memo[i - 1] != -1 && memo[i] > memo[i - 1] + 1))) {
            memo[i] = memo[i - 1] + 1
        }
    }
    for (i in 1000000 downTo 0) {
        if (i < 1000000) {
            if (memo[i] == -1 || (memo[i + 1] != -1 && memo[i] > memo[i + 1] + 1)) {
                memo[i] = memo[i + 1] + 1
            }
        }
    }
    println(memo[N])
}
