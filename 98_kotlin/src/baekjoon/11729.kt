// https://www.acmicpc.net/problem/11729
// 하노이 탑 이동 순서


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args: Array<String>) {
    val N = Integer.parseInt(BufferedReader(InputStreamReader(System.`in`)).readLine())
    val sb = StringBuffer()
    val cnt = Array(1) { 0 }
    hanoi(1, 3, 2, N, cnt, sb)
    println("${cnt[0]}\n${sb.toString()}")
}


fun hanoi(now: Int, dest: Int, temp: Int, disk: Int, cnt: Array<Int>, sb: StringBuffer) {
    if (disk == 0) return
    hanoi(now, temp, dest, disk - 1, cnt, sb)
    cnt[0]++
    sb.append("$now $dest\n")
    hanoi(temp, dest, now, disk - 1, cnt, sb)
}