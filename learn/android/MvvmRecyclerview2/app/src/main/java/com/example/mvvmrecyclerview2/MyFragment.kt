package com.example.mvvmrecyclerview2

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.fragment.app.Fragment
import androidx.lifecycle.LiveData
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import com.example.mvvmrecyclerview2.databinding.MyFragmentBinding


class MyFragment : Fragment() {

    companion object {
        val TAG: String = "MyFragment"
    }

    private lateinit var adapter: MyAdapter
    private lateinit var binding: MyFragmentBinding

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        binding = DataBindingUtil.inflate(inflater, R.layout.my_fragment, container, false)
        adapter = MyAdapter(myClickCallback)
        binding.itemsList.adapter = adapter

        return binding.root
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        val viewModel = ViewModelProviders.of(this).get(MyViewModel::class.java)

        binding.button.setOnClickListener {
            subscribeUi(viewModel.getMyData())
        }

        subscribeUi(viewModel.getMyData())
    }

    private fun subscribeUi(liveData: LiveData<List<MyData>>) {
        liveData.observe(this,
            Observer<List<MyData>> { adapter.updateMyDataList(it) }
        )

    }


    private val myClickCallback: MyClickCallback = object : MyClickCallback {
        override fun onClick(myData: MyData) {
            (activity as MainActivity).showToast(myData)
        }

    }

}
