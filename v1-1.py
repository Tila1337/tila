�
    �>d,   �                   ��  � d dl mZ d dlmZ d dlmZmZmZmZ d dl	m
Z
mZmZmZ d dlmZ d dlmZmZ d dlmZmZmZ d dlZd dlZd dlZd dlZd d	lmZ d dlZd dlZd dlZd dlZd d
lmZm Z m!Z!  ej"        d��  �         d dlm"Z"mZ  e"�   �          d� Z# e#�   �          ej$        Z%ej&        Z'ej(        Z)ej*        Z+ej,        Z-ej.        Z/e'e)e+e-e/gZ0d� Z1 e1�   �           e2dd�  �        5 Z3 ee3�  �        Z4 e5e4�  �        Z6dZ7dZ8e6e7dz
           e8dz
           Z9ddd�  �         n# 1 swxY w Y    e:e9�  �        Z;e;dz   a< e2dd�  �        5 Z= ee=�  �        Z4 e5e4�  �        Z6e;Z7dZ8e6e7dz
           e8dz
           Z>ddd�  �         n# 1 swxY w Y    e:d�  �        Z? e@d�  �        ZAe>ZB ejC        �   �         ZDeD�E                    d�  �         eDd         d         ZFdZGd� ZH eH�   �          dS )�    )�TelegramClient)�GetDialogsRequest)�InputPeerEmpty�InputPeerChannel�InputPeerUser�PeerUser)�PeerFloodError�UserPrivacyRestrictedError�ChatWriteForbiddenError�UserAlreadyParticipantError)�InviteToChannelRequest)�GetFullChannelRequest�JoinChannelRequest)�types�utils�errorsN)�reader)�Fore�Back�StyleT)�	autoreset)�initr   c                  �l  � t          �   �         } d� }d� } |�   �           |�   �          t          ddd��  �        5 }t          j        |�  �        }t          ddd��  �        5 }t          j        |d	d
��  �        }|�                    g d��  �         d}|D ]G}|dz  }|�                    ||d         |d         |d         |d         |d         |d         f�  �         �H	 d d d �  �         n# 1 swxY w Y   d d d �  �         n# 1 swxY w Y   t          j        d�  �         t          j        d�  �         d S )Nc                  ��  � t          �   �         } t          ddd��  �        5 }t          j        |�  �        }|D ]7}| �                    |�  �         |D ]}|dk    r| �                    |�  �         ��8	 d d d �  �         n# 1 swxY w Y   t          ddd��  �        5 }t          j        |dd	�
�  �        }|�                    | �  �         d d d �  �         d S # 1 swxY w Y   d S )N�data.csv�r�UTF-8��encoding� �1.csv�w�,�
��	delimiter�lineterminator��list�open�csvr   �append�remove�writer�	writerows��lines�readFiler   �row�field�	writeFiler.   s          �!/storage/emulated/0/ramex/v1-1.py�mainzraj.<locals>.main   sy  � ������*�c�G�4�4�4� 	*���Z��)�)�F�� *� *�����S�!�!�!� � *� *�E���{�{����S�)�)�)��*�	*�		*� 	*� 	*� 	*� 	*� 	*� 	*� 	*� 	*� 	*� 	*���� 	*� 	*� 	*� 	*� �'�3��1�1�1� 	$�Y��Z�	�S��N�N�N�F����U�#�#�#�	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$���� 	$� 	$� 	$� 	$� 	$� 	$�$   �AA=�=B�B�-C�C�Cc                  ��  � t          �   �         } t          ddd��  �        5 }t          j        |�  �        }|D ]7}| �                    |�  �         |D ]}|dk    r| �                    |�  �         ��8	 d d d �  �         n# 1 swxY w Y   t          ddd��  �        5 }t          j        |dd	�
�  �        }|�                    | �  �         d d d �  �         d S # 1 swxY w Y   d S )Nr!   r   r   r   �username�2.csvr"   r#   r$   r%   r(   r0   s          r6   �main1zraj.<locals>.main1.   s{  � ������'�3��1�1�1� 	*�X��Z��)�)�F�� *� *�����S�!�!�!� � *� *�E��
�*�*����S�)�)�)��*�	*�		*� 	*� 	*� 	*� 	*� 	*� 	*� 	*� 	*� 	*� 	*���� 	*� 	*� 	*� 	*� �'�3��1�1�1� 	$�Y��Z�	�S��N�N�N�F����U�#�#�#�	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$� 	$���� 	$� 	$� 	$� 	$� 	$� 	$r8   r;   r   r   r   r   r"   r#   r$   r%   )zsr. no.r:   zuser id�access_hash�name�group�statusr   �   �   �   �   �   �   r!   )r)   r*   r+   r   r.   �writerow�osr-   )	r1   r7   r<   �source�rdr�fr.   �ir3   s	            r6   �rajrM      s�  � �	����$� $� $�($� $� $�* ����������
�7�C�'�*�*�*� 	U�f��j�� � ���*�c�G�4�4�4� 	U���Z��S��F�F�F�F��O�O�g�g�g�h�h�h��A�� U� U���Q�������C��F�C��F�C��F�C��F�C��F�C�PQ�F� S�T�T�T�T�U�		U� 	U� 	U� 	U� 	U� 	U� 	U� 	U� 	U� 	U� 	U���� 	U� 	U� 	U� 	U�	U� 	U� 	U� 	U� 	U� 	U� 	U� 	U� 	U� 	U� 	U���� 	U� 	U� 	U� 	U� ��7������7�����s6   �'D�"A;C*�D�*C.	�.D�1C.	�2D�D�Dc            	      �   � dd l } t          j        d�  �         t          dt          � dt
          � dt          � d��  �         d S )Nr   �clearr$   u�  

                     ┏━━━┳━━━┳┓╋╋┏┳━━┳┓
                     ┗┓┏┓┃┏━━┫┗┓┏┛┣┫┣┫┃
                     ╋┃┃┃┃┗━━╋┓┃┃┏┛┃┃┃┃
                     ╋┃┃┃┃┏━━┛┃┗┛┃╋┃┃┃┃╋┏┓
                     ┏┛┗┛┃┗━━┓┗┓┏┛┏┫┣┫┗━┛┃uU   
                     ┗━━━┻━━━┛╋┗┛╋┗━━┻━━━┛z

)�randomrH   �system�print�cy�yer   )rP   s    r6   �HackingZonepostrU   ]   sp   � ��M�M�M��I�g����	� 
��
� 
� VX�
� 
� VW�
� 
� 
� 
� 
� 
� 
� 
�    �
memory.csvr   rA   z	phone.csvi�$ � 7e14b38d250953c8c1e94fd7b2d63550z
config.ini�HackingZone�ToGroup�d   c                  �Z  � t           } t          j        t          �  �        }t	          d|� �t
          t          �  �        }|�                    �   �          |�                    �   �         s{t          t          j        t          j        z   dz   �  �         |�                    |�  �         |�                    |t!          t          j        t          j        z   dz   �  �        �  �         |�                    �   �         }|j        s|j        }n|j        dz   |j        z   }d}g }t+          |d��  �        5 }t-          j        |dd	�
�  �        }t1          |d �  �         |D ]R}	i }|	d         |d<   |	d         |d<   t3          |	d         �  �        |d<   |	d         |d<   |�                    |�  �         �S	 d d d �  �         n# 1 swxY w Y   t+          dd�  �        5 }
t/          |
�  �        }t7          |�  �        }d}d}||dz
           |dz
           }d d d �  �         n# 1 swxY w Y   t3          |�  �        }|dz   }t+          dd�  �        5 }
t/          |
�  �        }t7          |�  �        }d}d}||dz
           |dz
           }d d d �  �         n# 1 swxY w Y   t3          |�  �        }|dz   }t+          ddd��  �        5 }t-          j        |dd	�
�  �        }|�                    t<          ||g�  �         d d d �  �         n# 1 swxY w Y   |D �]�}t3          |�  �        t3          |d         �  �        k    �r�t3          |d         �  �        t3          |�  �        k    �r�	 d}|d         dk    rt          d�  �         �p |t?          | |d         g�  �        �  �         t          j        t          j        z   dz   }t          t          j        t          j         z   dz   �  �         tC          j"        tG          j$        d�  �        �  �         �n9# tJ          $ r3 t          j        t          j        z   dz   }tC          j"        d�  �         Y n�tL          $ r d}Y n�tN          $ rI}d}t          t          j        t          j         z   dz   �  �         tC          j"        d�  �         Y d }~n�d }~wtP          $ r7} |tS          | �  �        �  �         tC          j"        d �  �         Y d }~���d }~wtT          j+        $ r}|j,        j-        }Y d }~nAd }~wt\          $ r}|}Y d }~n-d }~w t_          j0        �   �          t          d!�  �         Y ��3xY w|�1                    | �  �        } |te          |�"�  �        �  �        }t3          |j3        j4        �  �        }t          t          j        t          j        z   d|� dt          j        t          j5        z   � d#|� t          j6        � dt          j        t          j7        z   � d$|d         � d%|� �z   �  �         ���t3          |d         �  �        t3          |�  �        k    r�t          t          j        t          j        z   d&z   �  �         t          t          j        t          j         z   d'z   �  �         t!          �   �         }|dk    rtq          �   �          ���ts          �   �          ���d S )(Nz	sessions/zsome thing has changedzEnter the code: � r   r   r   r#   r$   r%   r   �srnorA   r:   rB   �idrC   r>   rW   r   �2   r"   rY   r    zno username, moving to next�DONEzPlease Wait...�PrivacyRestrictedError�ALREADYr	   z(Script Are In Progress So Please Wait...rE   zUnexpected Error)�channelz > Group Members z>> z >> z
Members Added Successfully !
zPress Enter To Exit):�to_groupr   �parse_phone�pphoner   �api_id�api_hash�connect�is_user_authorizedrR   r   �BRIGHTr   �RED�send_code_request�sign_in�input�GREEN�get_me�	last_name�
first_namer*   r+   r   �next�intr,   r)   r.   rG   �	nextdeltar   �YELLOW�time�sleeprP   �	randranger
   r   r	   r   r   r   �RPCError�	__class__�__name__�	Exception�	traceback�	print_exc�
get_entityr   �	full_chat�participants_count�RESET�	RESET_ALL�CYAN�autos�quit) �channel_username�phone�client�user�
LegendName�
input_file�usersrK   �rowsr3   �hash_obj�
csv_reader�list_of_rows�
row_number�
col_number�numnext�	startfrom�	nextstart�numend�endto�nextend�dfr.   r@   �g�cwfe�e�d�channel_connect�channel_full_info�countt�stats                                    r6   r�   r�   �   s�  � �����f�%�%�E��/��/�/���B�B�F�
�N�N�����$�$�&�&� Y��e�l�T�X�%�(@�@�A�A�A�� � ��'�'�'����u�e���t�z�(A�DV�(V�W�W�X�X�X� �=�=�?�?�D��>� 9��_�
�
��_�c�)�$�.�8�
��J��E�	�j�7�	+�	+�	+� 
�q��z�!�s�4�@�@�@���T�4����� 	� 	�C��D��q�6�D��L�"�1�v�D����S��V���D��J��q�6�D��L��L�L������	�
� 
� 
� 
� 
� 
� 
� 
� 
� 
� 
���� 
� 
� 
� 
� 
�l�C�	 �	 � ?�H��H�%�%�
��J�'�'���
��
��z�A�~�.�z�A�~�>��?� ?� ?� ?� ?� ?� ?� ?� ?� ?� ?���� ?� ?� ?� ?� �G���I��"��I�	�l�C�	 �	 � >�H��H�%�%�
��J�'�'���
��
��j�1�n�-�j�1�n�=��>� >� >� >� >� >� >� >� >� >� >���� >� >� >� >� ��K�K�E��B�h�G�	�l�3��	0�	0�	0� 7�B���B�#�d�C�C�C������9�W�5�6�6�6�7� 7� 7� 7� 7� 7� 7� 7� 7� 7� 7���� 7� 7� 7� 7� � 5� 5���	�N�N�c�$�v�,�/�/�/�/�c�$�v�,�6G�6G�3�u�:�:�6U�6U�&�&���
�#�r�)�)��7�8�8�8����-�.>��Z�@P�?Q�R�R�S�S�S����
�2�V�;���e�l�T�[�0�3C�C�D�D�D��
�6�+�A�.�.�/�/�/�/��-� � � �����0�3K�K���
�1������.� #� #� #�"����!� � � �)���e�l�T�[�0�3]�]�^�^�^��
�1�������������*� � � ���)�*:�;�;�<�<�<��
�1��������������?� .� .� .���-������������ � � ��V�V�V�V�V�V�������#�%�%�%��(�)�)�)������$�/�/�0@�A�A�O� &��'<�_�'U�'U�'U� V� V���*�4�G�H�H�F��%�,���+�  .{��  .{�  .{�e�l�4�:�>U�  .{�  .{�io�  .{�rw�  sC�  .{�  .{�  FK�  FR�  SW�  S\�  F\�  .{�  .{�  ae�  fl�  am�  .{�  .{�  sy�  .{�  .{�  {�  |�  |�  |�  |���f�����U���+�+��%�,���+�.P�P�Q�Q�Q��%�,���,�/D�D�E�E�E��7�7�D��q�y�y�����������k5� 5s�   �,A=F6�6F:�=F:�7H�H�H�7J�J
�J
�75K8�8K<�?K<�P�5BP�:T8�>T8�	T8�?R�T8�%,S�T8�)S:�:T8�T�'T8)I�telethon.syncr   �telethon.tl.functions.messagesr   �telethon.tl.typesr   r   r   r   �telethon.errors.rpcerrorlistr	   r
   r   r   �telethon.tl.functions.channelsr   r   r   �telethonr   r   r   �configparser�sysrH   r+   r   r�   ry   rP   �coloramar   r   r   r   rM   r�   �n�LIGHTGREEN_EX�lgrm   r   �WHITEr"   r�   rS   rx   rT   �colorsrU   r*   r�   r�   r)   r�   r�   r�   �numdelrv   �deltarw   �read_obj�valuerh   �strri   rg   �ConfigParser�config�readre   �SLEEP_TIME_2r�   � rV   r6   �<module>r�      s�  �� (� (� (� (� (� (� <� <� <� <� <� <� W� W� W� W� W� W� W� W� W� W� W� W� J�  J�  J�  J�  J�  J�  J�  J�  J�  J�  J�  J� A� A� A� A� A� A� T� T� T� T� T� T� T� T� )� )� )� )� )� )� )� )� )� )� � � � � 
�
�
�
� 	�	�	�	� 
�
�
�
� � � � � � � � � � � ���� ���� ���� &� &� &� &� &� &� &� &� &� &� ���� � � � � � � � � � � � � �����<� <� <�| ������J��	����H���J��	�Y��	�[��
�a��B��	��� � � �� � � �	�T�,���� :�����!�!�J��4�
�#�#�L��J��J��*�q�.�)�*�q�.�9�F�:� :� :� :� :� :� :� :� :� :� :���� :� :� :� :� 	��F�����!�G�	�	�T�+�s��� 9�x����!�!�J��4�
�#�#�L��J��J���a��(��a��8�E�9� 9� 9� 9� 9� 9� 9� 9� 9� 9� 9���� 9� 9� 9� 9� 
��W�����3�1�2�2��	��	"��	"�	$�	$�� ���L� � � ��-� ��+����m� m� m�^ ������s$   �'/D"�"D&�)D&�	/F�F�F