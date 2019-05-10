package test

import io.reactivex.rxkotlin.toObservable
import org.junit.Test
import kotlin.test.assertTrue

class BlockingForEach {
    @Test
    fun `test with blockingForEach`() {
        val list = listOf(1, 4, 5, 7, 9, 90, 7, 4, 3, 2, 12, 23, 45, 7, 1)
        val observable = list.toObservable().filter { it % 2 == 0 }
        observable.forEach { assertTrue { it % 2 == 0 } }
    }
}