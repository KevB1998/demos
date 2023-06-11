TEMPLATE=$1
HEX=$2
FQBN='adafruit:samd:adafruit_metro_m0'
PORT='COM3'

cp "./templates/${TEMPLATE}/${TEMPLATE}.ino" rgb-matrix.ino
sed -i -e "s/HEX_ARRAY/${HEX}/g" rgb-matrix.ino
arduino compile rgb-matrix.ino --fqbn "$FQBN"
arduino upload rgb-matrix.ino --fqbn "$FQBN" --port "$PORT"