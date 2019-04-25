//  https://www.acmicpc.net/problem/11365
//  !밀비 급일

package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var s = br.readLine()
    val sb = StringBuffer()
    while (s != "END") {
        sb.append("${s.reversed()}\n")
        s = br.readLine()
    }
    println(sb.toString())
}