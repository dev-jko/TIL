package com.example.tictactoemvp.view

interface TicTacToeView {
    fun setButtonText(row: Int, col: Int, player: String)
    fun showWinner(winner: String)
    fun clearWinnerDisplay()
    fun clearButtons()



}
