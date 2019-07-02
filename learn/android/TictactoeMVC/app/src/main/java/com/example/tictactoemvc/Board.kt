package com.example.tictactoemvc

import com.example.tictactoemvc.Player.O
import com.example.tictactoemvc.Player.X

class Board {

    private val cells: Array<Array<Cell>> = Array(3) { Array(3) { Cell() } }
    var winner: Player? = null
    private var state: GameState = GameState.FINISHED
    private lateinit var currentTurn: Player

    private enum class GameState { IN_PROGRESS, FINISHED }

    init {
        restart()
    }

    fun restart() {
        clearCells()
        winner = null
        currentTurn = X
        state = GameState.IN_PROGRESS
    }

    private fun clearCells() {
        cells.forEach { it.forEach { cell -> cell.value = null } }
    }

    fun mark(row: Int, col: Int): Player? {
        var playerThatMoved: Player? = null

        if (isValid(row, col)) {
            cells[row][col].value = currentTurn
            playerThatMoved = currentTurn

            if (isWinningMoveByPlayer(currentTurn, row, col)) {
                state = GameState.FINISHED
                winner = currentTurn
            } else {
                flipCurrentTurn()
            }
        }
        return playerThatMoved
    }

    private fun isWinningMoveByPlayer(player: Player, currentRow: Int, currentCol: Int): Boolean {
        return (cells[currentRow][0].value == player
                && cells[currentRow][1].value == player
                && cells[currentRow][2].value == player
                || cells[0][currentCol].value == player
                && cells[1][currentCol].value == player
                && cells[2][currentCol].value == player
                || currentRow == currentCol
                && cells[0][0].value == player
                && cells[1][1].value == player
                && cells[2][2].value == player
                || currentRow + currentCol == 2
                && cells[0][2].value == player
                && cells[1][1].value == player
                && cells[2][0].value == player)
    }

    private fun flipCurrentTurn() {
        currentTurn = if (currentTurn == X) O else X
    }

    private fun isValid(row: Int, col: Int): Boolean {
        return when {
            state == GameState.FINISHED -> false
            isOutOfBounds(row) || isOutOfBounds(col) -> false
            isCellValueAlreadySet(row, col) -> false
            else -> true
        }
    }

    private fun isCellValueAlreadySet(row: Int, col: Int): Boolean {
        return cells[row][col].value != null
    }

    private fun isOutOfBounds(index: Int): Boolean {
        return index < 0 || index > 2
    }


}
