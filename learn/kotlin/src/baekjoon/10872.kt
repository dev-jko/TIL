// https://www.acmicpc.net/problem/10872
// 팩토리얼


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args: Array<String>) {
    val N = Integer.parseInt(BufferedReader(InputStreamReader(System.`in`)).readLine())
    val memo = Array<Int>(N + 1) { it }
    memo[0] = 1
    for (i in 1..N) {
        memo[i] *= memo[i - 1]
    }
    println(memo[N])
}