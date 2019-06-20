package com.example.mvvmrecyclerview2

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.recyclerview.widget.RecyclerView
import com.example.mvvmrecyclerview2.databinding.MyDataItemBinding

class MyAdapter(private val clickCallback: MyClickCallback) : RecyclerView.Adapter<MyAdapter.MyViewHolder>() {

    var myDataList: List<MyData>? = null

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val binding: MyDataItemBinding = DataBindingUtil
            .inflate(LayoutInflater.from(parent.context), R.layout.my_data_item, parent, false)
        binding.callback = clickCallback
        return MyViewHolder(binding)
    }

    override fun getItemCount(): Int {
        if (myDataList == null)
            return 0
        return myDataList!!.size
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        holder.binding.myData = myDataList!![position]
    }

    fun updateMyDataList(list: List<MyData>?) {
        if (list == null)
            return
        myDataList = list
        notifyDataSetChanged()
    }


    class MyViewHolder(val binding: MyDataItemBinding) : RecyclerView.ViewHolder(binding.root)

}
