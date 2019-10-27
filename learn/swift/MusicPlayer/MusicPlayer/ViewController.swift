//
//  ViewController.swift
//  MusicPlayer
//
//  Created by Jaedoo Ko on 2019/10/26.
//  Copyright © 2019 Jaedoo Ko. All rights reserved.
//

import UIKit
import AVFoundation

class ViewController: UIViewController, AVAudioPlayerDelegate {
    
    var player: AVAudioPlayer!
    var timer: Timer!
    
    var playPauseButton: UIButton!
    var timeLabel: UILabel!
    var progressSlider: UISlider!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.addViewsWithCode()
        self.initializePlayer()
    }
    
    func addViewsWithCode(){
        self.addPlayPauseButton()
        self.addTimerLabel()
        self.addProgressSlider()
    }
    
    func addPlayPauseButton(){
        let button:UIButton = UIButton(type: UIButton.ButtonType.custom)
        button.translatesAutoresizingMaskIntoConstraints = false
        
        self.view.addSubview(button)
        
        button.setImage(UIImage(named: "button_play"), for: UIControl.State.normal)
        button.setImage(UIImage(named: "button_pause"), for: UIControl.State.selected)
        
        button.addTarget(self, action: #selector(self.touchUpPlayPauseButton(_:)), for: UIControl.Event.touchUpInside)
        
        let centerX: NSLayoutConstraint = button.centerXAnchor.constraint(equalTo: self.view.centerXAnchor)
        let centerY: NSLayoutConstraint = NSLayoutConstraint(item: button, attribute: NSLayoutConstraint.Attribute.centerY, relatedBy: NSLayoutConstraint.Relation.equal, toItem: self.view, attribute: NSLayoutConstraint.Attribute.centerY, multiplier: 0.8, constant: 0)
        let width:NSLayoutConstraint = button.widthAnchor.constraint(equalTo: self.view.widthAnchor, multiplier: 0.5)
        let ratio: NSLayoutConstraint = button.heightAnchor.constraint(equalTo: button.widthAnchor, multiplier: 1)
        
        centerX.isActive = true
        centerY.isActive = true
        width.isActive = true
        ratio.isActive = true
        
        self.playPauseButton = button
    }
    
    func addTimerLabel(){
        let label: UILabel = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        
        self.view.addSubview(label)
        
        label.textColor = UIColor.black
        label.textAlignment = NSTextAlignment.center
        label.font = UIFont.preferredFont(forTextStyle: UIFont.TextStyle.headline)
        
        let centerX:NSLayoutConstraint = label.centerXAnchor.constraint(equalTo: self.playPauseButton.centerXAnchor)
        let top:NSLayoutConstraint = label.topAnchor.constraint(equalTo: self.playPauseButton.bottomAnchor, constant: 8)
        
        centerX.isActive = true
        top.isActive = true
        
        self.timeLabel = label
        self.updateTimeLabelText(time: 0)
    }
    
    func addProgressSlider(){
        let slider:UISlider = UISlider()
        slider.translatesAutoresizingMaskIntoConstraints = false
        
        self.view.addSubview(slider)
        
        slider.minimumTrackTintColor = UIColor.red
        
        slider.addTarget(self, action: #selector(self.sliderValueChanged(_:)), for: UIControl.Event.valueChanged)
        
        let safeAreaGuide:UILayoutGuide = self.view.safeAreaLayoutGuide
        let centerX:NSLayoutConstraint = slider.centerXAnchor.constraint(equalTo: self.timeLabel.centerXAnchor)
        let top: NSLayoutConstraint = slider.topAnchor.constraint(equalTo: self.timeLabel.bottomAnchor, constant: 8)
        let leading: NSLayoutConstraint = slider.leadingAnchor.constraint(equalTo: safeAreaGuide.leadingAnchor, constant: 16)
        let trailing: NSLayoutConstraint = slider.trailingAnchor.constraint(equalTo: safeAreaGuide.trailingAnchor, constant: -16)
        centerX.isActive = true
        top.isActive = true
        leading.isActive = true
        trailing.isActive = true
        
        self.progressSlider = slider
    }
    
    @IBAction func touchUpPlayPauseButton(_ sender: UIButton) {
        sender.isSelected = !sender.isSelected
        
        if sender.isSelected {
            self.player?.play()
        } else {
            self.player?.pause()
        }
        
        if sender.isSelected {
            self.makeAndFireTImer()
        } else {
            self.invalidateTimer()
        }
    }

    @IBAction func sliderValueChanged(_ sender: UISlider) {
        self.updateTimeLabelText(time: TimeInterval(sender.value))
        if sender.isTracking { return }
        self.player.currentTime = TimeInterval(sender.value)
    }
    
    func initializePlayer() {
        guard let soundAsset: NSDataAsset = NSDataAsset(name: "sound") else {
            print("음원 파일 에셋을 가져올 수 없습니다.")
            return
        }
        
        do {
            try self.player = AVAudioPlayer(data: soundAsset.data)
            self.player.delegate = self
        } catch let error as NSError {
            print("플레이어 초기화 실패")
            print("코드 : \(error.code), 메세지 : \(error.localizedDescription)")
        }
        
        self.progressSlider.maximumValue = Float(self.player.duration)
        self.progressSlider.minimumValue = 0
        self.progressSlider.value = Float(self.player.currentTime)
    }
    
    func updateTimeLabelText(time: TimeInterval){
        let minute:Int = Int(time/60)
        let seconde:Int = Int(time.truncatingRemainder(dividingBy: 60))
        let milisecond:Int = Int(time.truncatingRemainder(dividingBy: 1) * 100)
        
        let timeText: String = String(format: "%02ld:%02ld:%02ld", minute, seconde, milisecond)
        
        self.timeLabel.text = timeText
    }
    
    func makeAndFireTImer(){
        self.timer = Timer.scheduledTimer(withTimeInterval: 0.01, repeats: true, block: { [unowned self] (timer: Timer) in
            if self.progressSlider.isTracking { return }
            
            self.updateTimeLabelText(time: self.player.currentTime)
            self.progressSlider.value = Float(self.player.currentTime)
        })
        self.timer.fire()
    }
    
    func invalidateTimer(){
        self.timer.invalidate()
        self.timer = nil
    }
    
    func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer, error: Error?) {
        guard let error: Error = error else {
            print("오디오 플레이어 디코드 오류 발생")
            return
        }
        
        let message: String = "오디오 플레이어 오류 발생 \(error.localizedDescription)"
        let alert: UIAlertController = UIAlertController(title: "알림", message: message, preferredStyle: UIAlertController.Style.alert)
        let okAction: UIAlertAction = UIAlertAction(title: "확인", style: UIAlertAction.Style.default){ (action: UIAlertAction) -> Void in
            self.dismiss(animated: true, completion: nil)
        }
        
        alert.addAction(okAction)
        self.present(alert, animated: true, completion: nil)
    }
    
    func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer, successfully flag: Bool) {
        self.playPauseButton.isSelected = false
        self.progressSlider.value = 0
        self.updateTimeLabelText(time: 0)
        self.invalidateTimer()
    }
}

