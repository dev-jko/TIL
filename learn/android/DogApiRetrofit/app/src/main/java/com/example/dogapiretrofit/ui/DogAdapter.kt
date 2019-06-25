package com.example.dogapiretrofit.ui

import android.util.Log
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.dogapiretrofit.R
import com.example.dogapiretrofit.databinding.DogItemBinding

class DogAdapter(private val mDogClickCallback: DogClickCallback) : RecyclerView.Adapter<DogAdapter.DogItemHolder>() {

    var dogImgUrlList: MutableList<String> = MutableList(0) { "" }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): DogItemHolder {
        val binding: DogItemBinding = DataBindingUtil.inflate(
            LayoutInflater.from(parent.context),
            R.layout.dog_item, parent, false
        )
        binding.callback = mDogClickCallback
        return DogItemHolder(binding)
    }

    override fun getItemCount(): Int {
        return dogImgUrlList.size
    }

    override fun onBindViewHolder(holder: DogItemHolder, position: Int) {
        holder.binding.imgUrl = dogImgUrlList.get(position)
        holder.binding.position = position
        Glide.with(holder.binding.root).load(holder.binding.imgUrl).into(holder.binding.imageView)
    }

    fun changeDogImgUrlList(newList: List<String>) {
        dogImgUrlList.clear()
        dogImgUrlList.addAll(0, newList)
        notifyDataSetChanged()
    }

    fun addDogImgUrl(url: String, position: Int = dogImgUrlList.size) {
        Log.d("DogAdapter", dogImgUrlList.toString())
        dogImgUrlList.add(position, url)
        notifyItemInserted(position)
        Log.d("DogAdapter", dogImgUrlList.toString())
    }


    class DogItemHolder(val binding: DogItemBinding) : RecyclerView.ViewHolder(binding.root)

}