// https://www.acmicpc.net/problem/2523
// 별 찍기 - 13


package baekjoon

fun main(args: Array<String>) {
    val N = readLine()!!.toInt()
    val sb = StringBuffer()
    for (i in 1..N) {
        sb.append("${"*".repeat(i)}\n")
    }
    for (i in N - 1 downTo 1) {
        sb.append("${"*".repeat(i)}\n")
    }
    print(sb.toString())
}