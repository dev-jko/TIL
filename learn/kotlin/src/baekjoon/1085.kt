//  https://www.acmicpc.net/problem/1085
//  직사각형에서 탈출


package baekjoon

fun main(args: Array<String>) {
    val result = readLine()!!.split(" ").map { it.toInt() }.toMutableList()
    result[2] -= result[0]
    result[3] -= result[1]
    println("${result.min()}")
}
