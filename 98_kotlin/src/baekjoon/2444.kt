// https://www.acmicpc.net/problem/2444
// 별 찍기 - 7


package baekjoon


fun main(args: Array<String>) {
    val N = readLine()?.toInt()
    val sb = StringBuffer()
    for (i in 1..N!!) {
        sb.append("${" ".repeat(N - i)}${"*".repeat(i * 2 - 1)}\n")
    }
    for (i in 1 until N) {
        sb.append("${" ".repeat(i)}${"*".repeat((N - i) * 2 - 1)}\n")
    }
    print(sb.toString())
}