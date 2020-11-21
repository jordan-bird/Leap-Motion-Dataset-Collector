# LICENSE FOR THE ORIGINAL EXAMPLE SCRIPT:

################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.			   #
# Leap Motion proprietary and confidential. Not for distribution.			   #
# Use subject to the terms of the Leap Motion SDK Agreement available at	   #
# https://developer.leapmotion.com/sdk_agreement, or another agreement		   #
# between Leap Motion and you, your company or other organization.			   #
################################################################################

# DATASET COLLECTION FROM ORIGINAL EXAMPLE SCRIPT CREATED BY JORDAN BIRD

import Leap, sys, thread, time
import math
import numpy as np
import vg
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import time
import cv2
import os


startTime = str(int(round(time.time())))

print startTime

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 



#cam.stop()



label = "CAR"
subject = "JORDAN"
filename = label + "-" + subject + "-" + startTime + ".csv"
folderName = label + "-" + subject + "-" + startTime
print filename
os.mkdir(folderName)

print startTime



class SampleListener(Leap.Listener):

	finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
	bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
	state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
	

	def on_init(self, controller):
		#imagesAllowed = controller.config.get("tracking_images_mode") == 
		controller.set_policy(Leap.Controller.POLICY_IMAGES)

	def on_connect(self, controller):
		print "Connected"

		# Enable gestures
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_disconnect(self, controller):
		# Note: not dispatched when running in a debugger.
		print "Disconnected"

	def on_exit(self, controller):
		print "Exited"

	def on_frame(self, controller):
		#controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)
		time.sleep(0.25)
		
		# Get the most recent frame and report some basic information
		frame = controller.frame()

		#print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
		#	   frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

		
		# make everything -1 in case they don't exist
		if True:
			right_palm_position_x = 0
			right_palm_position_y = 0
			right_palm_position_z = 0
			right_palm_normal_x = 0
			right_palm_normal_y = 0
			right_palm_normal_z = 0
			right_hand_direction_x = 0
			right_hand_direction_y = 0
			right_hand_direction_z = 0
			right_palm_velocity_x = 0
			right_palm_velocity_y = 0
			right_palm_velocity_z = 0
			right_hand_pitch = 0
			right_hand_roll = 0
			right_hand_yaw = 0
			right_arm_direction_x = 0
			right_arm_direction_y = 0
			right_arm_direction_z = 0
			right_wrist_position_x = 0
			right_wrist_position_y = 0
			right_wrist_position_z = 0
			right_elbow_position_x = 0
			right_elbow_position_y = 0
			right_elbow_position_z = 0
			right_thumb_length = 0
			right_thumb_width = 0
			right_thumb_metacarpal_start_x = 0
			right_thumb_metacarpal_start_y = 0
			right_thumb_metacarpal_start_z = 0
			right_thumb_metacarpal_end_x = 0
			right_thumb_metacarpal_end_y = 0
			right_thumb_metacarpal_end_z = 0
			right_thumb_metacarpal_direction_x = 0
			right_thumb_metacarpal_direction_y = 0
			right_thumb_metacarpal_direction_z = 0
			right_thumb_proximal_start_x = 0
			right_thumb_proximal_start_y = 0
			right_thumb_proximal_start_z = 0
			right_thumb_proximal_end_x = 0
			right_thumb_proximal_end_y = 0
			right_thumb_proximal_end_z = 0
			right_thumb_proximal_direction_x = 0
			right_thumb_proximal_direction_y = 0
			right_thumb_proximal_direction_z = 0
			right_thumb_intermediate_start_x = 0
			right_thumb_intermediate_start_y = 0
			right_thumb_intermediate_start_z = 0
			right_thumb_intermediate_end_x = 0
			right_thumb_intermediate_end_y = 0
			right_thumb_intermediate_end_z = 0
			right_thumb_intermediate_direction_x = 0
			right_thumb_intermediate_direction_y = 0
			right_thumb_intermediate_direction_z = 0
			right_thumb_distal_start_x = 0
			right_thumb_distal_start_y = 0
			right_thumb_distal_start_z = 0
			right_thumb_distal_end_x = 0
			right_thumb_distal_end_y = 0
			right_thumb_distal_end_z = 0
			right_thumb_distal_direction_x = 0
			right_thumb_distal_direction_y = 0
			right_thumb_distal_direction_z = 0
			right_index_length = 0
			right_index_width = 0
			right_index_metacarpal_start_x = 0
			right_index_metacarpal_start_y = 0
			right_index_metacarpal_start_z = 0
			right_index_metacarpal_end_x = 0
			right_index_metacarpal_end_y = 0
			right_index_metacarpal_end_z = 0
			right_index_metacarpal_direction_x = 0
			right_index_metacarpal_direction_y = 0
			right_index_metacarpal_direction_z = 0
			right_index_proximal_start_x = 0
			right_index_proximal_start_y = 0
			right_index_proximal_start_z = 0
			right_index_proximal_end_x = 0
			right_index_proximal_end_y = 0
			right_index_proximal_end_z = 0
			right_index_proximal_direction_x = 0
			right_index_proximal_direction_y = 0
			right_index_proximal_direction_z = 0
			right_index_intermediate_start_x = 0
			right_index_intermediate_start_y = 0
			right_index_intermediate_start_z = 0
			right_index_intermediate_end_x = 0
			right_index_intermediate_end_y = 0
			right_index_intermediate_end_z = 0
			right_index_intermediate_direction_x = 0
			right_index_intermediate_direction_y = 0
			right_index_intermediate_direction_z = 0
			right_index_distal_start_x = 0
			right_index_distal_start_y = 0
			right_index_distal_start_z = 0
			right_index_distal_end_x = 0
			right_index_distal_end_y = 0
			right_index_distal_end_z = 0
			right_index_distal_direction_x = 0
			right_index_distal_direction_y = 0
			right_index_distal_direction_z = 0
			right_middle_length = 0
			right_middle_width = 0
			right_middle_metacarpal_start_x = 0
			right_middle_metacarpal_start_y = 0
			right_middle_metacarpal_start_z = 0
			right_middle_metacarpal_end_x = 0
			right_middle_metacarpal_end_y = 0
			right_middle_metacarpal_end_z = 0
			right_middle_metacarpal_direction_x = 0
			right_middle_metacarpal_direction_y = 0
			right_middle_metacarpal_direction_z = 0
			right_middle_proximal_start_x = 0
			right_middle_proximal_start_y = 0
			right_middle_proximal_start_z = 0
			right_middle_proximal_end_x = 0
			right_middle_proximal_end_y = 0
			right_middle_proximal_end_z = 0
			right_middle_proximal_direction_x = 0
			right_middle_proximal_direction_y = 0
			right_middle_proximal_direction_z = 0
			right_middle_intermediate_start_x = 0
			right_middle_intermediate_start_y = 0
			right_middle_intermediate_start_z = 0
			right_middle_intermediate_end_x = 0
			right_middle_intermediate_end_y = 0
			right_middle_intermediate_end_z = 0
			right_middle_intermediate_direction_x = 0
			right_middle_intermediate_direction_y = 0
			right_middle_intermediate_direction_z = 0
			right_middle_distal_start_x = 0
			right_middle_distal_start_y = 0
			right_middle_distal_start_z = 0
			right_middle_distal_end_x = 0
			right_middle_distal_end_y = 0
			right_middle_distal_end_z = 0
			right_middle_distal_direction_x = 0
			right_middle_distal_direction_y = 0
			right_middle_distal_direction_z = 0
			right_ring_length = 0
			right_ring_width = 0
			right_ring_metacarpal_start_x = 0
			right_ring_metacarpal_start_y = 0
			right_ring_metacarpal_start_z = 0
			right_ring_metacarpal_end_x = 0
			right_ring_metacarpal_end_y = 0
			right_ring_metacarpal_end_z = 0
			right_ring_metacarpal_direction_x = 0
			right_ring_metacarpal_direction_y = 0
			right_ring_metacarpal_direction_z = 0
			right_ring_proximal_start_x = 0
			right_ring_proximal_start_y = 0
			right_ring_proximal_start_z = 0
			right_ring_proximal_end_x = 0
			right_ring_proximal_end_y = 0
			right_ring_proximal_end_z = 0
			right_ring_proximal_direction_x = 0
			right_ring_proximal_direction_y = 0
			right_ring_proximal_direction_z = 0
			right_ring_intermediate_start_x = 0
			right_ring_intermediate_start_y = 0
			right_ring_intermediate_start_z = 0
			right_ring_intermediate_end_x = 0
			right_ring_intermediate_end_y = 0
			right_ring_intermediate_end_z = 0
			right_ring_intermediate_direction_x = 0
			right_ring_intermediate_direction_y = 0
			right_ring_intermediate_direction_z = 0
			right_ring_distal_start_x = 0
			right_ring_distal_start_y = 0
			right_ring_distal_start_z = 0
			right_ring_distal_end_x = 0
			right_ring_distal_end_y = 0
			right_ring_distal_end_z = 0
			right_ring_distal_direction_x = 0
			right_ring_distal_direction_y = 0
			right_ring_distal_direction_z = 0
			right_pinky_length = 0
			right_pinky_width = 0
			right_pinky_metacarpal_start_x = 0
			right_pinky_metacarpal_start_y = 0
			right_pinky_metacarpal_start_z = 0
			right_pinky_metacarpal_end_x = 0
			right_pinky_metacarpal_end_y = 0
			right_pinky_metacarpal_end_z = 0
			right_pinky_metacarpal_direction_x = 0
			right_pinky_metacarpal_direction_y = 0
			right_pinky_metacarpal_direction_z = 0
			right_pinky_proximal_start_x = 0
			right_pinky_proximal_start_y = 0
			right_pinky_proximal_start_z = 0
			right_pinky_proximal_end_x = 0
			right_pinky_proximal_end_y = 0
			right_pinky_proximal_end_z = 0
			right_pinky_proximal_direction_x = 0
			right_pinky_proximal_direction_y = 0
			right_pinky_proximal_direction_z = 0
			right_pinky_intermediate_start_x = 0
			right_pinky_intermediate_start_y = 0
			right_pinky_intermediate_start_z = 0
			right_pinky_intermediate_end_x = 0
			right_pinky_intermediate_end_y = 0
			right_pinky_intermediate_end_z = 0
			right_pinky_intermediate_direction_x = 0
			right_pinky_intermediate_direction_y = 0
			right_pinky_intermediate_direction_z = 0
			right_pinky_distal_start_x = 0
			right_pinky_distal_start_y = 0
			right_pinky_distal_start_z = 0
			right_pinky_distal_end_x = 0
			right_pinky_distal_end_y = 0
			right_pinky_distal_end_z = 0
			right_pinky_distal_direction_x = 0
			right_pinky_distal_direction_y = 0
			right_pinky_distal_direction_z = 0
			left_palm_position_x = 0
			left_palm_position_y = 0
			left_palm_position_z = 0
			left_palm_normal_x = 0
			left_palm_normal_y = 0
			left_palm_normal_z = 0
			left_hand_direction_x = 0
			left_hand_direction_y = 0
			left_hand_direction_z = 0
			left_palm_velocity_x = 0
			left_palm_velocity_y = 0
			left_palm_velocity_z = 0
			left_hand_pitch = 0
			left_hand_roll = 0
			left_hand_yaw = 0
			left_arm_direction_x = 0
			left_arm_direction_y = 0
			left_arm_direction_z = 0
			left_wrist_position_x = 0
			left_wrist_position_y = 0
			left_wrist_position_z = 0
			left_elbow_position_x = 0
			left_elbow_position_y = 0
			left_elbow_position_z = 0
			left_thumb_length = 0
			left_thumb_width = 0
			left_thumb_metacarpal_start_x = 0
			left_thumb_metacarpal_start_y = 0
			left_thumb_metacarpal_start_z = 0
			left_thumb_metacarpal_end_x = 0
			left_thumb_metacarpal_end_y = 0
			left_thumb_metacarpal_end_z = 0
			left_thumb_metacarpal_direction_x = 0
			left_thumb_metacarpal_direction_y = 0
			left_thumb_metacarpal_direction_z = 0
			left_thumb_proximal_start_x = 0
			left_thumb_proximal_start_y = 0
			left_thumb_proximal_start_z = 0
			left_thumb_proximal_end_x = 0
			left_thumb_proximal_end_y = 0
			left_thumb_proximal_end_z = 0
			left_thumb_proximal_direction_x = 0
			left_thumb_proximal_direction_y = 0
			left_thumb_proximal_direction_z = 0
			left_thumb_intermediate_start_x = 0
			left_thumb_intermediate_start_y = 0
			left_thumb_intermediate_start_z = 0
			left_thumb_intermediate_end_x = 0
			left_thumb_intermediate_end_y = 0
			left_thumb_intermediate_end_z = 0
			left_thumb_intermediate_direction_x = 0
			left_thumb_intermediate_direction_y = 0
			left_thumb_intermediate_direction_z = 0
			left_thumb_distal_start_x = 0
			left_thumb_distal_start_y = 0
			left_thumb_distal_start_z = 0
			left_thumb_distal_end_x = 0
			left_thumb_distal_end_y = 0
			left_thumb_distal_end_z = 0
			left_thumb_distal_direction_x = 0
			left_thumb_distal_direction_y = 0
			left_thumb_distal_direction_z = 0
			left_index_length = 0
			left_index_width = 0
			left_index_metacarpal_start_x = 0
			left_index_metacarpal_start_y = 0
			left_index_metacarpal_start_z = 0
			left_index_metacarpal_end_x = 0
			left_index_metacarpal_end_y = 0
			left_index_metacarpal_end_z = 0
			left_index_metacarpal_direction_x = 0
			left_index_metacarpal_direction_y = 0
			left_index_metacarpal_direction_z = 0
			left_index_proximal_start_x = 0
			left_index_proximal_start_y = 0
			left_index_proximal_start_z = 0
			left_index_proximal_end_x = 0
			left_index_proximal_end_y = 0
			left_index_proximal_end_z = 0
			left_index_proximal_direction_x = 0
			left_index_proximal_direction_y = 0
			left_index_proximal_direction_z = 0
			left_index_intermediate_start_x = 0
			left_index_intermediate_start_y = 0
			left_index_intermediate_start_z = 0
			left_index_intermediate_end_x = 0
			left_index_intermediate_end_y = 0
			left_index_intermediate_end_z = 0
			left_index_intermediate_direction_x = 0
			left_index_intermediate_direction_y = 0
			left_index_intermediate_direction_z = 0
			left_index_distal_start_x = 0
			left_index_distal_start_y = 0
			left_index_distal_start_z = 0
			left_index_distal_end_x = 0
			left_index_distal_end_y = 0
			left_index_distal_end_z = 0
			left_index_distal_direction_x = 0
			left_index_distal_direction_y = 0
			left_index_distal_direction_z = 0
			left_middle_length = 0
			left_middle_width = 0
			left_middle_metacarpal_start_x = 0
			left_middle_metacarpal_start_y = 0
			left_middle_metacarpal_start_z = 0
			left_middle_metacarpal_end_x = 0
			left_middle_metacarpal_end_y = 0
			left_middle_metacarpal_end_z = 0
			left_middle_metacarpal_direction_x = 0
			left_middle_metacarpal_direction_y = 0
			left_middle_metacarpal_direction_z = 0
			left_middle_proximal_start_x = 0
			left_middle_proximal_start_y = 0
			left_middle_proximal_start_z = 0
			left_middle_proximal_end_x = 0
			left_middle_proximal_end_y = 0
			left_middle_proximal_end_z = 0
			left_middle_proximal_direction_x = 0
			left_middle_proximal_direction_y = 0
			left_middle_proximal_direction_z = 0
			left_middle_intermediate_start_x = 0
			left_middle_intermediate_start_y = 0
			left_middle_intermediate_start_z = 0
			left_middle_intermediate_end_x = 0
			left_middle_intermediate_end_y = 0
			left_middle_intermediate_end_z = 0
			left_middle_intermediate_direction_x = 0
			left_middle_intermediate_direction_y = 0
			left_middle_intermediate_direction_z = 0
			left_middle_distal_start_x = 0
			left_middle_distal_start_y = 0
			left_middle_distal_start_z = 0
			left_middle_distal_end_x = 0
			left_middle_distal_end_y = 0
			left_middle_distal_end_z = 0
			left_middle_distal_direction_x = 0
			left_middle_distal_direction_y = 0
			left_middle_distal_direction_z = 0
			left_ring_length = 0
			left_ring_width = 0
			left_ring_metacarpal_start_x = 0
			left_ring_metacarpal_start_y = 0
			left_ring_metacarpal_start_z = 0
			left_ring_metacarpal_end_x = 0
			left_ring_metacarpal_end_y = 0
			left_ring_metacarpal_end_z = 0
			left_ring_metacarpal_direction_x = 0
			left_ring_metacarpal_direction_y = 0
			left_ring_metacarpal_direction_z = 0
			left_ring_proximal_start_x = 0
			left_ring_proximal_start_y = 0
			left_ring_proximal_start_z = 0
			left_ring_proximal_end_x = 0
			left_ring_proximal_end_y = 0
			left_ring_proximal_end_z = 0
			left_ring_proximal_direction_x = 0
			left_ring_proximal_direction_y = 0
			left_ring_proximal_direction_z = 0
			left_ring_intermediate_start_x = 0
			left_ring_intermediate_start_y = 0
			left_ring_intermediate_start_z = 0
			left_ring_intermediate_end_x = 0
			left_ring_intermediate_end_y = 0
			left_ring_intermediate_end_z = 0
			left_ring_intermediate_direction_x = 0
			left_ring_intermediate_direction_y = 0
			left_ring_intermediate_direction_z = 0
			left_ring_distal_start_x = 0
			left_ring_distal_start_y = 0
			left_ring_distal_start_z = 0
			left_ring_distal_end_x = 0
			left_ring_distal_end_y = 0
			left_ring_distal_end_z = 0
			left_ring_distal_direction_x = 0
			left_ring_distal_direction_y = 0
			left_ring_distal_direction_z = 0
			left_pinky_length = 0
			left_pinky_width = 0
			left_pinky_metacarpal_start_x = 0
			left_pinky_metacarpal_start_y = 0
			left_pinky_metacarpal_start_z = 0
			left_pinky_metacarpal_end_x = 0
			left_pinky_metacarpal_end_y = 0
			left_pinky_metacarpal_end_z = 0
			left_pinky_metacarpal_direction_x = 0
			left_pinky_metacarpal_direction_y = 0
			left_pinky_metacarpal_direction_z = 0
			left_pinky_proximal_start_x = 0
			left_pinky_proximal_start_y = 0
			left_pinky_proximal_start_z = 0
			left_pinky_proximal_end_x = 0
			left_pinky_proximal_end_y = 0
			left_pinky_proximal_end_z = 0
			left_pinky_proximal_direction_x = 0
			left_pinky_proximal_direction_y = 0
			left_pinky_proximal_direction_z = 0
			left_pinky_intermediate_start_x = 0
			left_pinky_intermediate_start_y = 0
			left_pinky_intermediate_start_z = 0
			left_pinky_intermediate_end_x = 0
			left_pinky_intermediate_end_y = 0
			left_pinky_intermediate_end_z = 0
			left_pinky_intermediate_direction_x = 0
			left_pinky_intermediate_direction_y = 0
			left_pinky_intermediate_direction_z = 0
			left_pinky_distal_start_x = 0
			left_pinky_distal_start_y = 0
			left_pinky_distal_start_z = 0
			left_pinky_distal_end_x = 0
			left_pinky_distal_end_y = 0
			left_pinky_distal_end_z = 0
			left_pinky_distal_direction_x = 0
			left_pinky_distal_direction_y = 0
			left_pinky_distal_direction_z = 0
			
		# Get hands
		# WE TREAT LEFT AS RIGHT AND VICE VERSA!!!
		# This is because the Leap is in HMD mode and it thinks the left hand is the right hand
		for hand in frame.hands:

			# you may need to switch these around depending on your Leap Motion 
			handType = "Left hand" if hand.is_left else "Right hand"
			
			
			timestamp = frame.timestamp
			
			
			if handType=="Left hand":		
				#palm stuff
				left_palm_position = hand.palm_position
				
				left_palm_position_x = left_palm_position[0]
				left_palm_position_y = left_palm_position[1]
				left_palm_position_z = left_palm_position[2]
				
				left_palm_normal_x = hand.palm_normal[0]
				left_palm_normal_y = hand.palm_normal[1]
				left_palm_normal_z = hand.palm_normal[2]

				left_hand_direction_x = hand.direction[0]
				left_hand_direction_y = hand.direction[1]
				left_hand_direction_z = hand.direction[2]
				
				left_palm_velocity_x = hand.palm_velocity[0]
				left_palm_velocity_y = hand.palm_velocity[1]
				left_palm_velocity_z = hand.palm_velocity[2]
				
				
				
				# Get the hand's normal vector and direction
				normal = hand.palm_normal
				direction = hand.direction
				
				left_hand_pitch = direction.pitch * Leap.RAD_TO_DEG
				left_hand_roll = normal.roll * Leap.RAD_TO_DEG
				left_hand_yaw = direction.yaw * Leap.RAD_TO_DEG
				
				#arm stuff
				arm = hand.arm
				
				left_arm_direction_x = arm.direction[0]
				left_arm_direction_y = arm.direction[1]
				left_arm_direction_z = arm.direction[2]
				
				left_wrist_position_x = arm.wrist_position[0]
				left_wrist_position_y = arm.wrist_position[1]
				left_wrist_position_z = arm.wrist_position[2]
				
				left_elbow_position_x = arm.elbow_position[0]
				left_elbow_position_y = arm.elbow_position[1]
				left_elbow_position_z = arm.elbow_position[2]
				
				

				for finger in hand.fingers:
				# this needs to repeat
					if self.finger_names[finger.type] == "Thumb":
						#print "Left Thumb!"
						left_thumb_length = finger.length
						left_thumb_width = finger.width
						
						left_thumb_velocity = finger.tip_velocity #ignore this
						left_thumb_tip_position = finger.tip_position #ignore this
						
						
					
					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							left_thumb_metacarpal_start_x = bone.prev_joint[0]
							left_thumb_metacarpal_start_y = bone.prev_joint[1]
							left_thumb_metacarpal_start_z = bone.prev_joint[2]
							#end 
							left_thumb_metacarpal_end_x = bone.next_joint[0]
							left_thumb_metacarpal_end_y = bone.next_joint[1]
							left_thumb_metacarpal_end_z = bone.next_joint[2]
							#direction 
							left_thumb_metacarpal_direction_x = bone.direction[0]
							left_thumb_metacarpal_direction_y = bone.direction[1]
							left_thumb_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							left_thumb_proximal_start_x = bone.prev_joint[0]
							left_thumb_proximal_start_y = bone.prev_joint[1]
							left_thumb_proximal_start_z = bone.prev_joint[2]
							#end 
							left_thumb_proximal_end_x = bone.next_joint[0]
							left_thumb_proximal_end_y = bone.next_joint[1]
							left_thumb_proximal_end_z = bone.next_joint[2]
							#direction 
							left_thumb_proximal_direction_x = bone.direction[0]
							left_thumb_proximal_direction_y = bone.direction[1]
							left_thumb_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							left_thumb_intermediate_start_x = bone.prev_joint[0]
							left_thumb_intermediate_start_y = bone.prev_joint[1]
							left_thumb_intermediate_start_z = bone.prev_joint[2]
							#end 
							left_thumb_intermediate_end_x = bone.next_joint[0]
							left_thumb_intermediate_end_y = bone.next_joint[1]
							left_thumb_intermediate_end_z = bone.next_joint[2]
							#direction 
							left_thumb_intermediate_direction_x = bone.direction[0]
							left_thumb_intermediate_direction_y = bone.direction[1]
							left_thumb_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							left_thumb_distal_start_x = bone.prev_joint[0]
							left_thumb_distal_start_y = bone.prev_joint[1]
							left_thumb_distal_start_z = bone.prev_joint[2]
							#end 
							left_thumb_distal_end_x = bone.next_joint[0]
							left_thumb_distal_end_y = bone.next_joint[1]
							left_thumb_distal_end_z = bone.next_joint[2]
							#direction 
							left_thumb_distal_direction_x = bone.direction[0]
							left_thumb_distal_direction_y = bone.direction[1]
							left_thumb_distal_direction_z = bone.direction[2]
						
						
					if self.finger_names[finger.type] == "Index":
						#print "Left Index!"
						left_index_length = finger.length
						left_index_width = finger.width
						
						
						left_index_velocity = finger.tip_velocity #ignore this
						left_index_tip_position = finger.tip_position #ignore this
						
					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							left_index_metacarpal_start_x = bone.prev_joint[0]
							left_index_metacarpal_start_y = bone.prev_joint[1]
							left_index_metacarpal_start_z = bone.prev_joint[2]
							#end 
							left_index_metacarpal_end_x = bone.next_joint[0]
							left_index_metacarpal_end_y = bone.next_joint[1]
							left_index_metacarpal_end_z = bone.next_joint[2]
							#direction 
							left_index_metacarpal_direction_x = bone.direction[0]
							left_index_metacarpal_direction_y = bone.direction[1]
							left_index_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							left_index_proximal_start_x = bone.prev_joint[0]
							left_index_proximal_start_y = bone.prev_joint[1]
							left_index_proximal_start_z = bone.prev_joint[2]
							#end 
							left_index_proximal_end_x = bone.next_joint[0]
							left_index_proximal_end_y = bone.next_joint[1]
							left_index_proximal_end_z = bone.next_joint[2]
							#direction 
							left_index_proximal_direction_x = bone.direction[0]
							left_index_proximal_direction_y = bone.direction[1]
							left_index_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							left_index_intermediate_start_x = bone.prev_joint[0]
							left_index_intermediate_start_y = bone.prev_joint[1]
							left_index_intermediate_start_z = bone.prev_joint[2]
							#end 
							left_index_intermediate_end_x = bone.next_joint[0]
							left_index_intermediate_end_y = bone.next_joint[1]
							left_index_intermediate_end_z = bone.next_joint[2]
							#direction 
							left_index_intermediate_direction_x = bone.direction[0]
							left_index_intermediate_direction_y = bone.direction[1]
							left_index_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							left_index_distal_start_x = bone.prev_joint[0]
							left_index_distal_start_y = bone.prev_joint[1]
							left_index_distal_start_z = bone.prev_joint[2]
							#end 
							left_index_distal_end_x = bone.next_joint[0]
							left_index_distal_end_y = bone.next_joint[1]
							left_index_distal_end_z = bone.next_joint[2]
							#direction 
							left_index_distal_direction_x = bone.direction[0]
							left_index_distal_direction_y = bone.direction[1]
							left_index_distal_direction_z = bone.direction[2]
		
		
					if self.finger_names[finger.type] == "Middle":
						#print "Left Middle!"
						left_middle_length = finger.length
						left_middle_width = finger.width
						
						
						left_middle_velocity = finger.tip_velocity #ignore this
						left_middle_tip_position = finger.tip_position #ignore this
						
					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							left_middle_metacarpal_start_x = bone.prev_joint[0]
							left_middle_metacarpal_start_y = bone.prev_joint[1]
							left_middle_metacarpal_start_z = bone.prev_joint[2]
							#end 
							left_middle_metacarpal_end_x = bone.next_joint[0]
							left_middle_metacarpal_end_y = bone.next_joint[1]
							left_middle_metacarpal_end_z = bone.next_joint[2]
							#direction 
							left_middle_metacarpal_direction_x = bone.direction[0]
							left_middle_metacarpal_direction_y = bone.direction[1]
							left_middle_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							left_middle_proximal_start_x = bone.prev_joint[0]
							left_middle_proximal_start_y = bone.prev_joint[1]
							left_middle_proximal_start_z = bone.prev_joint[2]
							#end 
							left_middle_proximal_end_x = bone.next_joint[0]
							left_middle_proximal_end_y = bone.next_joint[1]
							left_middle_proximal_end_z = bone.next_joint[2]
							#direction 
							left_middle_proximal_direction_x = bone.direction[0]
							left_middle_proximal_direction_y = bone.direction[1]
							left_middle_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							left_middle_intermediate_start_x = bone.prev_joint[0]
							left_middle_intermediate_start_y = bone.prev_joint[1]
							left_middle_intermediate_start_z = bone.prev_joint[2]
							#end 
							left_middle_intermediate_end_x = bone.next_joint[0]
							left_middle_intermediate_end_y = bone.next_joint[1]
							left_middle_intermediate_end_z = bone.next_joint[2]
							#direction 
							left_middle_intermediate_direction_x = bone.direction[0]
							left_middle_intermediate_direction_y = bone.direction[1]
							left_middle_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							left_middle_distal_start_x = bone.prev_joint[0]
							left_middle_distal_start_y = bone.prev_joint[1]
							left_middle_distal_start_z = bone.prev_joint[2]
							#end 
							left_middle_distal_end_x = bone.next_joint[0]
							left_middle_distal_end_y = bone.next_joint[1]
							left_middle_distal_end_z = bone.next_joint[2]
							#direction 
							left_middle_distal_direction_x = bone.direction[0]
							left_middle_distal_direction_y = bone.direction[1]
							left_middle_distal_direction_z = bone.direction[2]
		
		
					if self.finger_names[finger.type] == "Ring":
						#print "Left Ring!"
						left_ring_length = finger.length
						left_ring_width = finger.width
						
						
						left_ring_velocity = finger.tip_velocity #ignore this
						left_ring_tip_position = finger.tip_position #ignore this
						
					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							left_ring_metacarpal_start_x = bone.prev_joint[0]
							left_ring_metacarpal_start_y = bone.prev_joint[1]
							left_ring_metacarpal_start_z = bone.prev_joint[2]
							#end 
							left_ring_metacarpal_end_x = bone.next_joint[0]
							left_ring_metacarpal_end_y = bone.next_joint[1]
							left_ring_metacarpal_end_z = bone.next_joint[2]
							#direction 
							left_ring_metacarpal_direction_x = bone.direction[0]
							left_ring_metacarpal_direction_y = bone.direction[1]
							left_ring_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							left_ring_proximal_start_x = bone.prev_joint[0]
							left_ring_proximal_start_y = bone.prev_joint[1]
							left_ring_proximal_start_z = bone.prev_joint[2]
							#end 
							left_ring_proximal_end_x = bone.next_joint[0]
							left_ring_proximal_end_y = bone.next_joint[1]
							left_ring_proximal_end_z = bone.next_joint[2]
							#direction 
							left_ring_proximal_direction_x = bone.direction[0]
							left_ring_proximal_direction_y = bone.direction[1]
							left_ring_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							left_ring_intermediate_start_x = bone.prev_joint[0]
							left_ring_intermediate_start_y = bone.prev_joint[1]
							left_ring_intermediate_start_z = bone.prev_joint[2]
							#end 
							left_ring_intermediate_end_x = bone.next_joint[0]
							left_ring_intermediate_end_y = bone.next_joint[1]
							left_ring_intermediate_end_z = bone.next_joint[2]
							#direction 
							left_ring_intermediate_direction_x = bone.direction[0]
							left_ring_intermediate_direction_y = bone.direction[1]
							left_ring_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							left_ring_distal_start_x = bone.prev_joint[0]
							left_ring_distal_start_y = bone.prev_joint[1]
							left_ring_distal_start_z = bone.prev_joint[2]
							#end 
							left_ring_distal_end_x = bone.next_joint[0]
							left_ring_distal_end_y = bone.next_joint[1]
							left_ring_distal_end_z = bone.next_joint[2]
							#direction 
							left_ring_distal_direction_x = bone.direction[0]
							left_ring_distal_direction_y = bone.direction[1]
							left_ring_distal_direction_z = bone.direction[2]
		
		
					if self.finger_names[finger.type] == "Pinky":
						#print "Left Pinky!"
						left_pinky_length = finger.length
						left_pinky_width = finger.width
						
						
						left_pinky_velocity = finger.tip_velocity #ignore this
						left_pinky_tip_position = finger.tip_position #ignore this
						

					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							left_pinky_metacarpal_start_x = bone.prev_joint[0]
							left_pinky_metacarpal_start_y = bone.prev_joint[1]
							left_pinky_metacarpal_start_z = bone.prev_joint[2]
							#end 
							left_pinky_metacarpal_end_x = bone.next_joint[0]
							left_pinky_metacarpal_end_y = bone.next_joint[1]
							left_pinky_metacarpal_end_z = bone.next_joint[2]
							#direction 
							left_pinky_metacarpal_direction_x = bone.direction[0]
							left_pinky_metacarpal_direction_y = bone.direction[1]
							left_pinky_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							left_pinky_proximal_start_x = bone.prev_joint[0]
							left_pinky_proximal_start_y = bone.prev_joint[1]
							left_pinky_proximal_start_z = bone.prev_joint[2]
							#end 
							left_pinky_proximal_end_x = bone.next_joint[0]
							left_pinky_proximal_end_y = bone.next_joint[1]
							left_pinky_proximal_end_z = bone.next_joint[2]
							#direction 
							left_pinky_proximal_direction_x = bone.direction[0]
							left_pinky_proximal_direction_y = bone.direction[1]
							left_pinky_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							left_pinky_intermediate_start_x = bone.prev_joint[0]
							left_pinky_intermediate_start_y = bone.prev_joint[1]
							left_pinky_intermediate_start_z = bone.prev_joint[2]
							#end 
							left_pinky_intermediate_end_x = bone.next_joint[0]
							left_pinky_intermediate_end_y = bone.next_joint[1]
							left_pinky_intermediate_end_z = bone.next_joint[2]
							#direction 
							left_pinky_intermediate_direction_x = bone.direction[0]
							left_pinky_intermediate_direction_y = bone.direction[1]
							left_pinky_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							left_pinky_distal_start_x = bone.prev_joint[0]
							left_pinky_distal_start_y = bone.prev_joint[1]
							left_pinky_distal_start_z = bone.prev_joint[2]
							#end 
							left_pinky_distal_end_x = bone.next_joint[0]
							left_pinky_distal_end_y = bone.next_joint[1]
							left_pinky_distal_end_z = bone.next_joint[2]
							#direction 
							left_pinky_distal_direction_x = bone.direction[0]
							left_pinky_distal_direction_y = bone.direction[1]
							left_pinky_distal_direction_z = bone.direction[2]
		
			if handType=="Right hand":		
				#palm stuff
				right_palm_position = hand.palm_position
				
				right_palm_position_x = right_palm_position[0]
				right_palm_position_y = right_palm_position[1]
				right_palm_position_z = right_palm_position[2]
				
				right_palm_normal_x = hand.palm_normal[0]
				right_palm_normal_y = hand.palm_normal[1]
				right_palm_normal_z = hand.palm_normal[2]

				right_hand_direction_x = hand.direction[0]
				right_hand_direction_y = hand.direction[1]
				right_hand_direction_z = hand.direction[2]
				
				right_palm_velocity_x = hand.palm_velocity[0]
				right_palm_velocity_y = hand.palm_velocity[1]
				right_palm_velocity_z = hand.palm_velocity[2]
				
				
				
				# Get the hand's normal vector and direction
				normal = hand.palm_normal
				direction = hand.direction
				
				right_hand_pitch = direction.pitch * Leap.RAD_TO_DEG
				right_hand_roll = normal.roll * Leap.RAD_TO_DEG
				right_hand_yaw = direction.yaw * Leap.RAD_TO_DEG
				
				#arm stuff
				arm = hand.arm
				
				right_arm_direction_x = arm.direction[0]
				right_arm_direction_y = arm.direction[1]
				right_arm_direction_z = arm.direction[2]
				
				right_wrist_position_x = arm.wrist_position[0]
				right_wrist_position_y = arm.wrist_position[1]
				right_wrist_position_z = arm.wrist_position[2]
				
				right_elbow_position_x = arm.elbow_position[0]
				right_elbow_position_y = arm.elbow_position[1]
				right_elbow_position_z = arm.elbow_position[2]
				
				

				for finger in hand.fingers:
				# this needs to repeat
					if self.finger_names[finger.type] == "Thumb":
						#print "Right Thumb!"
						right_thumb_length = finger.length
						right_thumb_width = finger.width
						
						
						right_thumb_velocity = finger.tip_velocity #ignore this
						right_thumb_tip_position = finger.tip_position #ignore this
					
					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							right_thumb_metacarpal_start_x = bone.prev_joint[0]
							right_thumb_metacarpal_start_y = bone.prev_joint[1]
							right_thumb_metacarpal_start_z = bone.prev_joint[2]
							#end 
							right_thumb_metacarpal_end_x = bone.next_joint[0]
							right_thumb_metacarpal_end_y = bone.next_joint[1]
							right_thumb_metacarpal_end_z = bone.next_joint[2]
							#direction 
							right_thumb_metacarpal_direction_x = bone.direction[0]
							right_thumb_metacarpal_direction_y = bone.direction[1]
							right_thumb_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							right_thumb_proximal_start_x = bone.prev_joint[0]
							right_thumb_proximal_start_y = bone.prev_joint[1]
							right_thumb_proximal_start_z = bone.prev_joint[2]
							#end 
							right_thumb_proximal_end_x = bone.next_joint[0]
							right_thumb_proximal_end_y = bone.next_joint[1]
							right_thumb_proximal_end_z = bone.next_joint[2]
							#direction 
							right_thumb_proximal_direction_x = bone.direction[0]
							right_thumb_proximal_direction_y = bone.direction[1]
							right_thumb_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							right_thumb_intermediate_start_x = bone.prev_joint[0]
							right_thumb_intermediate_start_y = bone.prev_joint[1]
							right_thumb_intermediate_start_z = bone.prev_joint[2]
							#end 
							right_thumb_intermediate_end_x = bone.next_joint[0]
							right_thumb_intermediate_end_y = bone.next_joint[1]
							right_thumb_intermediate_end_z = bone.next_joint[2]
							#direction 
							right_thumb_intermediate_direction_x = bone.direction[0]
							right_thumb_intermediate_direction_y = bone.direction[1]
							right_thumb_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							right_thumb_distal_start_x = bone.prev_joint[0]
							right_thumb_distal_start_y = bone.prev_joint[1]
							right_thumb_distal_start_z = bone.prev_joint[2]
							#end 
							right_thumb_distal_end_x = bone.next_joint[0]
							right_thumb_distal_end_y = bone.next_joint[1]
							right_thumb_distal_end_z = bone.next_joint[2]
							#direction 
							right_thumb_distal_direction_x = bone.direction[0]
							right_thumb_distal_direction_y = bone.direction[1]
							right_thumb_distal_direction_z = bone.direction[2]
						
						
					if self.finger_names[finger.type] == "Index":
						#print "Right Index!"
						right_index_length = finger.length
						right_index_width = finger.width
						
						
						right_index_velocity = finger.tip_velocity #ignore this
						right_index_tip_position = finger.tip_position #ignore this
						
					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							right_index_metacarpal_start_x = bone.prev_joint[0]
							right_index_metacarpal_start_y = bone.prev_joint[1]
							right_index_metacarpal_start_z = bone.prev_joint[2]
							#end 
							right_index_metacarpal_end_x = bone.next_joint[0]
							right_index_metacarpal_end_y = bone.next_joint[1]
							right_index_metacarpal_end_z = bone.next_joint[2]
							#direction 
							right_index_metacarpal_direction_x = bone.direction[0]
							right_index_metacarpal_direction_y = bone.direction[1]
							right_index_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							right_index_proximal_start_x = bone.prev_joint[0]
							right_index_proximal_start_y = bone.prev_joint[1]
							right_index_proximal_start_z = bone.prev_joint[2]
							#end 
							right_index_proximal_end_x = bone.next_joint[0]
							right_index_proximal_end_y = bone.next_joint[1]
							right_index_proximal_end_z = bone.next_joint[2]
							#direction 
							right_index_proximal_direction_x = bone.direction[0]
							right_index_proximal_direction_y = bone.direction[1]
							right_index_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							right_index_intermediate_start_x = bone.prev_joint[0]
							right_index_intermediate_start_y = bone.prev_joint[1]
							right_index_intermediate_start_z = bone.prev_joint[2]
							#end 
							right_index_intermediate_end_x = bone.next_joint[0]
							right_index_intermediate_end_y = bone.next_joint[1]
							right_index_intermediate_end_z = bone.next_joint[2]
							#direction 
							right_index_intermediate_direction_x = bone.direction[0]
							right_index_intermediate_direction_y = bone.direction[1]
							right_index_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							right_index_distal_start_x = bone.prev_joint[0]
							right_index_distal_start_y = bone.prev_joint[1]
							right_index_distal_start_z = bone.prev_joint[2]
							#end 
							right_index_distal_end_x = bone.next_joint[0]
							right_index_distal_end_y = bone.next_joint[1]
							right_index_distal_end_z = bone.next_joint[2]
							#direction 
							right_index_distal_direction_x = bone.direction[0]
							right_index_distal_direction_y = bone.direction[1]
							right_index_distal_direction_z = bone.direction[2]
		
		
					if self.finger_names[finger.type] == "Middle":
						#print "Right Middle!"
						right_middle_length = finger.length
						right_middle_width = finger.width
						
						
						right_middle_velocity = finger.tip_velocity #ignore this
						right_middle_tip_position = finger.tip_position #ignore this
						
					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							right_middle_metacarpal_start_x = bone.prev_joint[0]
							right_middle_metacarpal_start_y = bone.prev_joint[1]
							right_middle_metacarpal_start_z = bone.prev_joint[2]
							#end 
							right_middle_metacarpal_end_x = bone.next_joint[0]
							right_middle_metacarpal_end_y = bone.next_joint[1]
							right_middle_metacarpal_end_z = bone.next_joint[2]
							#direction 
							right_middle_metacarpal_direction_x = bone.direction[0]
							right_middle_metacarpal_direction_y = bone.direction[1]
							right_middle_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							right_middle_proximal_start_x = bone.prev_joint[0]
							right_middle_proximal_start_y = bone.prev_joint[1]
							right_middle_proximal_start_z = bone.prev_joint[2]
							#end 
							right_middle_proximal_end_x = bone.next_joint[0]
							right_middle_proximal_end_y = bone.next_joint[1]
							right_middle_proximal_end_z = bone.next_joint[2]
							#direction 
							right_middle_proximal_direction_x = bone.direction[0]
							right_middle_proximal_direction_y = bone.direction[1]
							right_middle_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							right_middle_intermediate_start_x = bone.prev_joint[0]
							right_middle_intermediate_start_y = bone.prev_joint[1]
							right_middle_intermediate_start_z = bone.prev_joint[2]
							#end 
							right_middle_intermediate_end_x = bone.next_joint[0]
							right_middle_intermediate_end_y = bone.next_joint[1]
							right_middle_intermediate_end_z = bone.next_joint[2]
							#direction 
							right_middle_intermediate_direction_x = bone.direction[0]
							right_middle_intermediate_direction_y = bone.direction[1]
							right_middle_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							right_middle_distal_start_x = bone.prev_joint[0]
							right_middle_distal_start_y = bone.prev_joint[1]
							right_middle_distal_start_z = bone.prev_joint[2]
							#end 
							right_middle_distal_end_x = bone.next_joint[0]
							right_middle_distal_end_y = bone.next_joint[1]
							right_middle_distal_end_z = bone.next_joint[2]
							#direction 
							right_middle_distal_direction_x = bone.direction[0]
							right_middle_distal_direction_y = bone.direction[1]
							right_middle_distal_direction_z = bone.direction[2]
		
		
					if self.finger_names[finger.type] == "Ring":
						#print "Right Ring!"
						right_ring_length = finger.length
						right_ring_width = finger.width
						
						
						right_ring_velocity = finger.tip_velocity #ignore this
						right_ring_tip_position = finger.tip_position #ignore this
						
					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							right_ring_metacarpal_start_x = bone.prev_joint[0]
							right_ring_metacarpal_start_y = bone.prev_joint[1]
							right_ring_metacarpal_start_z = bone.prev_joint[2]
							#end 
							right_ring_metacarpal_end_x = bone.next_joint[0]
							right_ring_metacarpal_end_y = bone.next_joint[1]
							right_ring_metacarpal_end_z = bone.next_joint[2]
							#direction 
							right_ring_metacarpal_direction_x = bone.direction[0]
							right_ring_metacarpal_direction_y = bone.direction[1]
							right_ring_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							right_ring_proximal_start_x = bone.prev_joint[0]
							right_ring_proximal_start_y = bone.prev_joint[1]
							right_ring_proximal_start_z = bone.prev_joint[2]
							#end 
							right_ring_proximal_end_x = bone.next_joint[0]
							right_ring_proximal_end_y = bone.next_joint[1]
							right_ring_proximal_end_z = bone.next_joint[2]
							#direction 
							right_ring_proximal_direction_x = bone.direction[0]
							right_ring_proximal_direction_y = bone.direction[1]
							right_ring_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							right_ring_intermediate_start_x = bone.prev_joint[0]
							right_ring_intermediate_start_y = bone.prev_joint[1]
							right_ring_intermediate_start_z = bone.prev_joint[2]
							#end 
							right_ring_intermediate_end_x = bone.next_joint[0]
							right_ring_intermediate_end_y = bone.next_joint[1]
							right_ring_intermediate_end_z = bone.next_joint[2]
							#direction 
							right_ring_intermediate_direction_x = bone.direction[0]
							right_ring_intermediate_direction_y = bone.direction[1]
							right_ring_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							right_ring_distal_start_x = bone.prev_joint[0]
							right_ring_distal_start_y = bone.prev_joint[1]
							right_ring_distal_start_z = bone.prev_joint[2]
							#end 
							right_ring_distal_end_x = bone.next_joint[0]
							right_ring_distal_end_y = bone.next_joint[1]
							right_ring_distal_end_z = bone.next_joint[2]
							#direction 
							right_ring_distal_direction_x = bone.direction[0]
							right_ring_distal_direction_y = bone.direction[1]
							right_ring_distal_direction_z = bone.direction[2]
		
		
					if self.finger_names[finger.type] == "Pinky":
						#print "Right Pinky!"
						right_pinky_length = finger.length
						right_pinky_width = finger.width
						
						
						right_pinky_velocity = finger.tip_velocity #ignore this
						right_pinky_tip_position = finger.tip_position #ignore this
						

					for b in range(0, 4):
						if b==0:
							bone = finger.bone(b)
							#start
							right_pinky_metacarpal_start_x = bone.prev_joint[0]
							right_pinky_metacarpal_start_y = bone.prev_joint[1]
							right_pinky_metacarpal_start_z = bone.prev_joint[2]
							#end 
							right_pinky_metacarpal_end_x = bone.next_joint[0]
							right_pinky_metacarpal_end_y = bone.next_joint[1]
							right_pinky_metacarpal_end_z = bone.next_joint[2]
							#direction 
							right_pinky_metacarpal_direction_x = bone.direction[0]
							right_pinky_metacarpal_direction_y = bone.direction[1]
							right_pinky_metacarpal_direction_z = bone.direction[2]
						if b==1:
							bone = finger.bone(b)
							#start
							right_pinky_proximal_start_x = bone.prev_joint[0]
							right_pinky_proximal_start_y = bone.prev_joint[1]
							right_pinky_proximal_start_z = bone.prev_joint[2]
							#end 
							right_pinky_proximal_end_x = bone.next_joint[0]
							right_pinky_proximal_end_y = bone.next_joint[1]
							right_pinky_proximal_end_z = bone.next_joint[2]
							#direction 
							right_pinky_proximal_direction_x = bone.direction[0]
							right_pinky_proximal_direction_y = bone.direction[1]
							right_pinky_proximal_direction_z = bone.direction[2]
						if b==2:
							bone = finger.bone(b)
							#start
							right_pinky_intermediate_start_x = bone.prev_joint[0]
							right_pinky_intermediate_start_y = bone.prev_joint[1]
							right_pinky_intermediate_start_z = bone.prev_joint[2]
							#end 
							right_pinky_intermediate_end_x = bone.next_joint[0]
							right_pinky_intermediate_end_y = bone.next_joint[1]
							right_pinky_intermediate_end_z = bone.next_joint[2]
							#direction 
							right_pinky_intermediate_direction_x = bone.direction[0]
							right_pinky_intermediate_direction_y = bone.direction[1]
							right_pinky_intermediate_direction_z = bone.direction[2]
						if b==3:
							bone = finger.bone(b)
							#start
							right_pinky_distal_start_x = bone.prev_joint[0]
							right_pinky_distal_start_y = bone.prev_joint[1]
							right_pinky_distal_start_z = bone.prev_joint[2]
							#end 
							right_pinky_distal_end_x = bone.next_joint[0]
							right_pinky_distal_end_y = bone.next_joint[1]
							right_pinky_distal_end_z = bone.next_joint[2]
							#direction 
							right_pinky_distal_direction_x = bone.direction[0]
							right_pinky_distal_direction_y = bone.direction[1]
							right_pinky_distal_direction_z = bone.direction[2]
		
		
		if not (frame.hands.is_empty and frame.gestures().is_empty):
			
			ret,frame = cap.read() # return a single frame in variable `frame`
			frame = cv2.resize(frame, (256,256))
			imageName = folderName + '/' + str(time.time()) + '.png'
			cv2.imwrite(imageName,frame)
			
			recorded_variables = [left_palm_position_x,left_palm_position_y,left_palm_position_z,left_palm_normal_x,left_palm_normal_y,left_palm_normal_z,left_hand_direction_x,left_hand_direction_y,left_hand_direction_z,left_palm_velocity_x,left_palm_velocity_y,left_palm_velocity_z,left_hand_pitch,left_hand_roll,left_hand_yaw,left_arm_direction_x,left_arm_direction_y,left_arm_direction_z,left_wrist_position_x,left_wrist_position_y,left_wrist_position_z,left_elbow_position_x,left_elbow_position_y,left_elbow_position_z,left_thumb_length,left_thumb_width,left_thumb_metacarpal_start_x,left_thumb_metacarpal_start_y,left_thumb_metacarpal_start_z,left_thumb_metacarpal_end_x,left_thumb_metacarpal_end_y,left_thumb_metacarpal_end_z,left_thumb_metacarpal_direction_x,left_thumb_metacarpal_direction_y,left_thumb_metacarpal_direction_z,left_thumb_proximal_start_x,left_thumb_proximal_start_y,left_thumb_proximal_start_z,left_thumb_proximal_end_x,left_thumb_proximal_end_y,left_thumb_proximal_end_z,left_thumb_proximal_direction_x,left_thumb_proximal_direction_y,left_thumb_proximal_direction_z,left_thumb_intermediate_start_x,left_thumb_intermediate_start_y,left_thumb_intermediate_start_z,left_thumb_intermediate_end_x,left_thumb_intermediate_end_y,left_thumb_intermediate_end_z,left_thumb_intermediate_direction_x,left_thumb_intermediate_direction_y,left_thumb_intermediate_direction_z,left_thumb_distal_start_x,left_thumb_distal_start_y,left_thumb_distal_start_z,left_thumb_distal_end_x,left_thumb_distal_end_y,left_thumb_distal_end_z,left_thumb_distal_direction_x,left_thumb_distal_direction_y,left_thumb_distal_direction_z,left_index_length,left_index_width,left_index_metacarpal_start_x,left_index_metacarpal_start_y,left_index_metacarpal_start_z,left_index_metacarpal_end_x,left_index_metacarpal_end_y,left_index_metacarpal_end_z,left_index_metacarpal_direction_x,left_index_metacarpal_direction_y,left_index_metacarpal_direction_z,left_index_proximal_start_x,left_index_proximal_start_y,left_index_proximal_start_z,left_index_proximal_end_x,left_index_proximal_end_y,left_index_proximal_end_z,left_index_proximal_direction_x,left_index_proximal_direction_y,left_index_proximal_direction_z,left_index_intermediate_start_x,left_index_intermediate_start_y,left_index_intermediate_start_z,left_index_intermediate_end_x,left_index_intermediate_end_y,left_index_intermediate_end_z,left_index_intermediate_direction_x,left_index_intermediate_direction_y,left_index_intermediate_direction_z,left_index_distal_start_x,left_index_distal_start_y,left_index_distal_start_z,left_index_distal_end_x,left_index_distal_end_y,left_index_distal_end_z,left_index_distal_direction_x,left_index_distal_direction_y,left_index_distal_direction_z,left_middle_length,left_middle_width,left_middle_metacarpal_start_x,left_middle_metacarpal_start_y,left_middle_metacarpal_start_z,left_middle_metacarpal_end_x,left_middle_metacarpal_end_y,left_middle_metacarpal_end_z,left_middle_metacarpal_direction_x,left_middle_metacarpal_direction_y,left_middle_metacarpal_direction_z,left_middle_proximal_start_x,left_middle_proximal_start_y,left_middle_proximal_start_z,left_middle_proximal_end_x,left_middle_proximal_end_y,left_middle_proximal_end_z,left_middle_proximal_direction_x,left_middle_proximal_direction_y,left_middle_proximal_direction_z,left_middle_intermediate_start_x,left_middle_intermediate_start_y,left_middle_intermediate_start_z,left_middle_intermediate_end_x,left_middle_intermediate_end_y,left_middle_intermediate_end_z,left_middle_intermediate_direction_x,left_middle_intermediate_direction_y,left_middle_intermediate_direction_z,left_middle_distal_start_x,left_middle_distal_start_y,left_middle_distal_start_z,left_middle_distal_end_x,left_middle_distal_end_y,left_middle_distal_end_z,left_middle_distal_direction_x,left_middle_distal_direction_y,left_middle_distal_direction_z,left_ring_length,left_ring_width,left_ring_metacarpal_start_x,left_ring_metacarpal_start_y,left_ring_metacarpal_start_z,left_ring_metacarpal_end_x,left_ring_metacarpal_end_y,left_ring_metacarpal_end_z,left_ring_metacarpal_direction_x,left_ring_metacarpal_direction_y,left_ring_metacarpal_direction_z,left_ring_proximal_start_x,left_ring_proximal_start_y,left_ring_proximal_start_z,left_ring_proximal_end_x,left_ring_proximal_end_y,left_ring_proximal_end_z,left_ring_proximal_direction_x,left_ring_proximal_direction_y,left_ring_proximal_direction_z,left_ring_intermediate_start_x,left_ring_intermediate_start_y,left_ring_intermediate_start_z,left_ring_intermediate_end_x,left_ring_intermediate_end_y,left_ring_intermediate_end_z,left_ring_intermediate_direction_x,left_ring_intermediate_direction_y,left_ring_intermediate_direction_z,left_ring_distal_start_x,left_ring_distal_start_y,left_ring_distal_start_z,left_ring_distal_end_x,left_ring_distal_end_y,left_ring_distal_end_z,left_ring_distal_direction_x,left_ring_distal_direction_y,left_ring_distal_direction_z,left_pinky_length,left_pinky_width,left_pinky_metacarpal_start_x,left_pinky_metacarpal_start_y,left_pinky_metacarpal_start_z,left_pinky_metacarpal_end_x,left_pinky_metacarpal_end_y,left_pinky_metacarpal_end_z,left_pinky_metacarpal_direction_x,left_pinky_metacarpal_direction_y,left_pinky_metacarpal_direction_z,left_pinky_proximal_start_x,left_pinky_proximal_start_y,left_pinky_proximal_start_z,left_pinky_proximal_end_x,left_pinky_proximal_end_y,left_pinky_proximal_end_z,left_pinky_proximal_direction_x,left_pinky_proximal_direction_y,left_pinky_proximal_direction_z,left_pinky_intermediate_start_x,left_pinky_intermediate_start_y,left_pinky_intermediate_start_z,left_pinky_intermediate_end_x,left_pinky_intermediate_end_y,left_pinky_intermediate_end_z,left_pinky_intermediate_direction_x,left_pinky_intermediate_direction_y,left_pinky_intermediate_direction_z,left_pinky_distal_start_x,left_pinky_distal_start_y,left_pinky_distal_start_z,left_pinky_distal_end_x,left_pinky_distal_end_y,left_pinky_distal_end_z,left_pinky_distal_direction_x,left_pinky_distal_direction_y,left_pinky_distal_direction_z,right_palm_position_x,right_palm_position_y,right_palm_position_z,right_palm_normal_x,right_palm_normal_y,right_palm_normal_z,right_hand_direction_x,right_hand_direction_y,right_hand_direction_z,right_palm_velocity_x,right_palm_velocity_y,right_palm_velocity_z,right_hand_pitch,right_hand_roll,right_hand_yaw,right_arm_direction_x,right_arm_direction_y,right_arm_direction_z,right_wrist_position_x,right_wrist_position_y,right_wrist_position_z,right_elbow_position_x,right_elbow_position_y,right_elbow_position_z,right_thumb_length,right_thumb_width,right_thumb_metacarpal_start_x,right_thumb_metacarpal_start_y,right_thumb_metacarpal_start_z,right_thumb_metacarpal_end_x,right_thumb_metacarpal_end_y,right_thumb_metacarpal_end_z,right_thumb_metacarpal_direction_x,right_thumb_metacarpal_direction_y,right_thumb_metacarpal_direction_z,right_thumb_proximal_start_x,right_thumb_proximal_start_y,right_thumb_proximal_start_z,right_thumb_proximal_end_x,right_thumb_proximal_end_y,right_thumb_proximal_end_z,right_thumb_proximal_direction_x,right_thumb_proximal_direction_y,right_thumb_proximal_direction_z,right_thumb_intermediate_start_x,right_thumb_intermediate_start_y,right_thumb_intermediate_start_z,right_thumb_intermediate_end_x,right_thumb_intermediate_end_y,right_thumb_intermediate_end_z,right_thumb_intermediate_direction_x,right_thumb_intermediate_direction_y,right_thumb_intermediate_direction_z,right_thumb_distal_start_x,right_thumb_distal_start_y,right_thumb_distal_start_z,right_thumb_distal_end_x,right_thumb_distal_end_y,right_thumb_distal_end_z,right_thumb_distal_direction_x,right_thumb_distal_direction_y,right_thumb_distal_direction_z,right_index_length,right_index_width,right_index_metacarpal_start_x,right_index_metacarpal_start_y,right_index_metacarpal_start_z,right_index_metacarpal_end_x,right_index_metacarpal_end_y,right_index_metacarpal_end_z,right_index_metacarpal_direction_x,right_index_metacarpal_direction_y,right_index_metacarpal_direction_z,right_index_proximal_start_x,right_index_proximal_start_y,right_index_proximal_start_z,right_index_proximal_end_x,right_index_proximal_end_y,right_index_proximal_end_z,right_index_proximal_direction_x,right_index_proximal_direction_y,right_index_proximal_direction_z,right_index_intermediate_start_x,right_index_intermediate_start_y,right_index_intermediate_start_z,right_index_intermediate_end_x,right_index_intermediate_end_y,right_index_intermediate_end_z,right_index_intermediate_direction_x,right_index_intermediate_direction_y,right_index_intermediate_direction_z,right_index_distal_start_x,right_index_distal_start_y,right_index_distal_start_z,right_index_distal_end_x,right_index_distal_end_y,right_index_distal_end_z,right_index_distal_direction_x,right_index_distal_direction_y,right_index_distal_direction_z,right_middle_length,right_middle_width,right_middle_metacarpal_start_x,right_middle_metacarpal_start_y,right_middle_metacarpal_start_z,right_middle_metacarpal_end_x,right_middle_metacarpal_end_y,right_middle_metacarpal_end_z,right_middle_metacarpal_direction_x,right_middle_metacarpal_direction_y,right_middle_metacarpal_direction_z,right_middle_proximal_start_x,right_middle_proximal_start_y,right_middle_proximal_start_z,right_middle_proximal_end_x,right_middle_proximal_end_y,right_middle_proximal_end_z,right_middle_proximal_direction_x,right_middle_proximal_direction_y,right_middle_proximal_direction_z,right_middle_intermediate_start_x,right_middle_intermediate_start_y,right_middle_intermediate_start_z,right_middle_intermediate_end_x,right_middle_intermediate_end_y,right_middle_intermediate_end_z,right_middle_intermediate_direction_x,right_middle_intermediate_direction_y,right_middle_intermediate_direction_z,right_middle_distal_start_x,right_middle_distal_start_y,right_middle_distal_start_z,right_middle_distal_end_x,right_middle_distal_end_y,right_middle_distal_end_z,right_middle_distal_direction_x,right_middle_distal_direction_y,right_middle_distal_direction_z,right_ring_length,right_ring_width,right_ring_metacarpal_start_x,right_ring_metacarpal_start_y,right_ring_metacarpal_start_z,right_ring_metacarpal_end_x,right_ring_metacarpal_end_y,right_ring_metacarpal_end_z,right_ring_metacarpal_direction_x,right_ring_metacarpal_direction_y,right_ring_metacarpal_direction_z,right_ring_proximal_start_x,right_ring_proximal_start_y,right_ring_proximal_start_z,right_ring_proximal_end_x,right_ring_proximal_end_y,right_ring_proximal_end_z,right_ring_proximal_direction_x,right_ring_proximal_direction_y,right_ring_proximal_direction_z,right_ring_intermediate_start_x,right_ring_intermediate_start_y,right_ring_intermediate_start_z,right_ring_intermediate_end_x,right_ring_intermediate_end_y,right_ring_intermediate_end_z,right_ring_intermediate_direction_x,right_ring_intermediate_direction_y,right_ring_intermediate_direction_z,right_ring_distal_start_x,right_ring_distal_start_y,right_ring_distal_start_z,right_ring_distal_end_x,right_ring_distal_end_y,right_ring_distal_end_z,right_ring_distal_direction_x,right_ring_distal_direction_y,right_ring_distal_direction_z,right_pinky_length,right_pinky_width,right_pinky_metacarpal_start_x,right_pinky_metacarpal_start_y,right_pinky_metacarpal_start_z,right_pinky_metacarpal_end_x,right_pinky_metacarpal_end_y,right_pinky_metacarpal_end_z,right_pinky_metacarpal_direction_x,right_pinky_metacarpal_direction_y,right_pinky_metacarpal_direction_z,right_pinky_proximal_start_x,right_pinky_proximal_start_y,right_pinky_proximal_start_z,right_pinky_proximal_end_x,right_pinky_proximal_end_y,right_pinky_proximal_end_z,right_pinky_proximal_direction_x,right_pinky_proximal_direction_y,right_pinky_proximal_direction_z,right_pinky_intermediate_start_x,right_pinky_intermediate_start_y,right_pinky_intermediate_start_z,right_pinky_intermediate_end_x,right_pinky_intermediate_end_y,right_pinky_intermediate_end_z,right_pinky_intermediate_direction_x,right_pinky_intermediate_direction_y,right_pinky_intermediate_direction_z,right_pinky_distal_start_x,right_pinky_distal_start_y,right_pinky_distal_start_z,right_pinky_distal_end_x,right_pinky_distal_end_y,right_pinky_distal_end_z,right_pinky_distal_direction_x,right_pinky_distal_direction_y,right_pinky_distal_direction_z]
			line = ""
			for attribute in recorded_variables:
				line = line + str(attribute) + ","
			
			line = line + "/" + imageName
			line = line + "," + label
			
			#img = cam.get_image()
			#pygame.image.save(img, ste(time.time()) + ".jpg")
			
			
			
			line = line + "\n"
			
			with open(filename, "a") as dataset:
				dataset.write(line)
			
			print "Recorded:" + str(time.time())
			#print line
			

def main():
	# Create a sample listener and controller
	listener = SampleListener()
	controller = Leap.Controller()

	# Have the sample listener receive events from the controller
	controller.add_listener(listener)

	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		# Remove the sample listener when done
		controller.remove_listener(listener)


if __name__ == "__main__":
	main()
