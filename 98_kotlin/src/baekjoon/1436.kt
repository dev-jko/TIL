// https://www.acmicpc.net/problem/1436
// 영화감독 숌


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args: Array<String>) {
    var N = Integer.parseInt(BufferedReader(InputStreamReader(System.`in`)).readLine())
    val result = ArrayList<Int>()
    var i = 666
    while (N > 0) {
        if (isEndNum(i)) {
            N--
            result.add(i)
        }
        i++
    }
    println(result.last())
}

fun isEndNum(num: Int): Boolean {
    val string = num.toString()
    var cnt = 0
    for (i in 0 until string.length) {
        if (string[i] == '6') {
            cnt++
        } else {
            cnt = 0
        }
        if (cnt == 3) {
            return true
        }
    }
    return false
}