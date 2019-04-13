//  https://www.acmicpc.net/problem/2178
//  미로 탐색


package baekjoon

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*


fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val miro = Array<String>(N) { br.readLine() }
    val visited = Array(N) { Array(M) { -1 } }
    val queue = LinkedList<Pair<Int, Int>>()
    val dxy = listOf(Pair(-1, 0), Pair(1, 0), Pair(0, -1), Pair(0, 1))
    queue.add(Pair(0, 0))
    visited[0][0] = 1
    while (queue.isNotEmpty()) {
        val (x, y) = queue.poll()
        for ((dx, dy) in dxy) {
            val nx = x + dx
            val ny = y + dy
            if (nx in 0 until N && ny in 0 until M && miro[nx][ny] == '1' && visited[nx][ny] == -1) {
                visited[nx][ny] = visited[x][y] + 1
                queue.add(Pair(nx, ny))
            }
        }
    }
    println(visited.last().last())
}