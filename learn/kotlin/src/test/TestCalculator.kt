package test

import org.junit.Test
import kotlin.test.assertEquals

fun add(a: Int, b: Int): Int {
    return a + b
}

fun substract(a: Int, b: Int): Int = a - b
fun mult(a: Int, b: Int): Int = a * b
fun divide(a: Int, b: Int): Int = a / b


class TestCalculator {
    @Test
    fun `addition test`() {
        assertEquals(1 + 2, add(1, 2))
    }

    @Test
    fun `substraction test`() {
        assertEquals(8 - 5, substract(8, 5))
    }

    @Test
    fun `multiplication test`() {
        assertEquals(4 * 2, mult(4, 2))
    }

    @Test
    fun `division test`() {
        assertEquals(8 / 2, divide(8, 2))
    }
}