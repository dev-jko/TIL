package test

import io.reactivex.rxkotlin.toObservable
import org.junit.Test
import kotlin.test.assertEquals

class BlockingIterable {

    @Test
    fun `test with blockingIterable`() {
        val list = listOf(2, 1, 5, 6, 7, 3, 2, 1, 4, 7, 3)
        val observable = list.toObservable().sorted()
        val iterable = observable.blockingIterable()
        assertEquals(list.sorted(), iterable.toList())
    }
}