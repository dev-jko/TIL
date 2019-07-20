package com.nadarm.boardmvvmrx.domain.interactor

import io.reactivex.Observable

interface FlowableUseCase<Params, Type> {
    fun execute(params: Params): Observable<Type>
}