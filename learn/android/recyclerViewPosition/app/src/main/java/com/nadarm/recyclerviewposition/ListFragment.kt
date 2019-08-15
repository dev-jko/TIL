package com.nadarm.recyclerviewposition


import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProviders
import androidx.navigation.fragment.findNavController
import com.nadarm.recyclerviewposition.databinding.FragmentListBinding
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.fragment_list.*


class ListFragment : Fragment() {

    private val compositeDisposable = CompositeDisposable()
    private lateinit var binding: FragmentListBinding
    private val vm: myViewModel by lazy { ViewModelProviders.of(this).get(myViewModel::class.java) }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        this.binding = DataBindingUtil.inflate(inflater, R.layout.fragment_list, container, false)
        this.binding.lifecycleOwner = this
        return this.binding.root
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)

        val adapter = MyAdapter()
        this.binding.adapter = adapter

        vm.subject
            .doOnSubscribe { println("doOnSubscribe") }
            .doOnNext { println("doOnNext") }
            .doOnComplete { println("doOnComplete") }
            .doFinally { println("finally") }
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(adapter::refresh)
            .addTo(this.compositeDisposable)

        button.setOnClickListener { this.startActivity2() }
    }

    private fun startActivity2() {
        this.findNavController().navigate(R.id.action_listFragment_to_textFragment)
    }

    override fun onDestroy() {
        super.onDestroy()
        this.compositeDisposable.clear()
    }

}
