//  https://www.acmicpc.net/problem/2751
//  수 정렬하기 2


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N = br.readLine().toInt()
    val nums = Array(2000001) { false }
    val sb = StringBuffer()
    for (i in 1..N) {
        val t = br.readLine().toInt() + 1000000
        nums[t] = true
    }
    for (i in 0..2000000) {
        if (nums[i]) {
            sb.append("${i-1000000}\n")
        }
    }
    print(sb.toString())
}
