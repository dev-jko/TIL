package com.example.tictactoemvp.presenter

import com.example.tictactoemvp.model.Board
import com.example.tictactoemvp.model.Player
import com.example.tictactoemvp.view.TicTacToeView

class TicTacToePresenter(private val view: TicTacToeView) : Presenter {

    private lateinit var model: Board

    override fun onCreate() {
        model = Board()
        onResetSelected()
    }

    override fun onPause() {
    }

    override fun onResume() {
    }

    override fun onDestroy() {
    }

    override fun onButtonSelected(row: Int, col: Int) {
        val playerThatMoved: Player? = model.mark(row, col)
        if (playerThatMoved != null) {
            view.setButtonText(row, col, playerThatMoved.toString())

            if (model.winner != null) {
                view.showWinner(playerThatMoved.toString())
            }
        }
    }

    override fun onResetSelected() {
        view.clearWinnerDisplay()
        view.clearButtons()
        model.restart()
    }


}