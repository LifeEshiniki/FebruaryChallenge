#音データの処理
import wave
import pyaudio

#　音声ファイルを読み込み再生する
def read_and_play():
    CHUNK = 1024

    #　test.wavを読み込みモードで開く
    with wave.open("test.wav","rb") as wf:

        # test.wavを再生
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),#ストリームを読み書きするときのデータ型
                        channels = wf.getnchannels(),#モノラルかステレオか　１でモノラル２でステレオ
                        rate = wf.getframerate(),#サンプリング周波数
                        output=True)#出力モード

        data = wf.readframes(CHUNK)

        while data != '':
            stream.write(data)#ストリームに書き込み
            data = wf.readframes(CHUNK)#次のデータを読み込む
        stream.stop_stream()
        stream.close()
    p.terminate()
    return

def main():
    read_and_play()

if __name__ == "__main__":
    main()
