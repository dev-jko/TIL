//  https://www.acmicpc.net/problem/10826
//  피보나치 수 4

package baekjoon

import java.math.BigInteger

fun main(args: Array<String>) {
    val n = readLine()!!.toInt()
    val memo: Array<BigInteger> = Array(n + 2) { BigInteger.ZERO }
    memo[1] = BigInteger.ONE
    for (i in 2..n) {
        memo[i] = memo[i - 1] + memo[i - 2]
    }
    println(memo[n])
}