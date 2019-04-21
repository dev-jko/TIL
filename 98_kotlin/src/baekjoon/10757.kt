//  https://www.acmicpc.net/problem/10757
//  큰 수 A+B

package baekjoon

import java.math.BigInteger

fun main(args: Array<String>) {
    val result = readLine()!!.split(" ").map { BigInteger(it) }.let { it[0] + it[1] }
    println(result)
}