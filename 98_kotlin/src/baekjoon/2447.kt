//  https://www.acmicpc.net/problem/2447
//  별 찍기 - 10

package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.log


fun main(args: Array<String>) {
    val N = Integer.parseInt(BufferedReader(InputStreamReader(System.`in`)).readLine())
    val k = log(N.toFloat(), 3f).toInt()
    val result = ArrayList<String>()
    val sb = StringBuffer()
    result.add("*")

    for (i in 0 until k) {
        star2447(result)
    }
    for (s in result) {
        sb.append("$s\n")
    }
    println(sb.toString())
}

fun star2447(arr: ArrayList<String>) {
    val len = arr[0].length
    val blank = " ".repeat(len)
    for (i in 0 until len) {
        arr.add(arr[i] + blank + arr[i])
    }
    for (i in 0 until len) {
        arr.add(arr[i].repeat(3))
    }
    for (i in 0 until len) {
        arr[i] = arr[i].repeat(3)
    }
}
