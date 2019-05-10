package test

import io.reactivex.rxkotlin.toObservable
import org.junit.Test
import kotlin.test.assertEquals

class BlockingGet {

    @Test
    fun `teset Single with blockingGet`() {
        val observable = listOf(1, 34, 6, 74, 34, 23, 31, 2, 8, 6).toObservable().sorted()
        val firstElement = observable.first(0)
        val firstItem = firstElement.blockingGet()
        assertEquals(1, firstItem)
    }

    @Test
    fun `test Maybe with blockingGet`() {
        val observable = listOf(2, 6, 7, 3, 2, 4, 7, 8, 821, 2, 1).toObservable().sorted()
        val firstElement = observable.firstElement()
        val firstItem = firstElement.blockingGet()
        assertEquals(1, firstItem)
    }
}