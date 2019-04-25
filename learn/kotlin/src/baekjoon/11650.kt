//  https://www.acmicpc.net/problem/11650
//  좌표 정렬하기

package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = Integer.parseInt(br.readLine())
    val pos:ArrayList<Array<Int>> = ArrayList()
    for (i in 1..n) {
        val s = br.readLine().split(" ")
        val a = Integer.parseInt(s[0])
        val b = Integer.parseInt(s[1])
        pos.add(arrayOf(a, b))
    }
    pos.sortBy { it[1] }
    pos.sortBy { it[0] }
    val sb = StringBuffer()
    for (p in pos) {
        sb.append("${p[0]} ${p[1]}\n")
    }
    println(sb.toString())
}