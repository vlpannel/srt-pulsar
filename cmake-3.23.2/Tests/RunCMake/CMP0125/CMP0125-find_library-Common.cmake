
find_library(RELATIVE_PATH NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)
find_library(RELATIVE_PATH_WITH_TYPE NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)

find_library(ABSOLUTE_PATH NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)
find_library(ABSOLUTE_PATH_WITH_TYPE NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)

find_library(NOTFOUND_PATH NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)
find_library(NOTFOUND_PATH_WITH_TYPE NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)

file(WRITE "${CMAKE_BINARY_DIR}/${FILE_NAME}" "")
file(CHMOD "${CMAKE_BINARY_DIR}/${FILE_NAME}" PERMISSIONS OWNER_EXECUTE OWNER_READ OWNER_WRITE)
find_library(FILE_NAME NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)
find_library(FILE_NAME_WITH_TYPE NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)

message("RELATIVE_PATH=${RELATIVE_PATH}")
message("RELATIVE_PATH_WITH_TYPE=${RELATIVE_PATH_WITH_TYPE}")

message("ABSOLUTE_PATH=${ABSOLUTE_PATH}")
message("ABSOLUTE_PATH_WITH_TYPE=${ABSOLUTE_PATH_WITH_TYPE}")

message("NOTFOUND_PATH=${NOTFOUND_PATH}")
message("NOTFOUND_PATH_WITH_TYPE=${NOTFOUND_PATH_WITH_TYPE}")

message("FILE_NAME=${FILE_NAME}")
message("FILE_NAME_WITH_TYPE=${FILE_NAME_WITH_TYPE}")


set(RELATIVE_PATH_AND_LOCAL relative_local)
set(RELATIVE_PATH_WITH_TYPE_AND_LOCAL relative_local)
set(ABSOLUTE_PATH_AND_LOCAL /absolute_local)
set(ABSOLUTE_PATH_WITH_TYPE_AND_LOCAL /absolute_local)
set(NOTFOUND_AND_LOCAL "${FILE_NAME}")
set(NOTFOUND_WITH_TYPE_AND_LOCAL "${FILE_NAME}")

find_library(RELATIVE_PATH_AND_LOCAL NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)
find_library(RELATIVE_PATH_WITH_TYPE_AND_LOCAL NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)

find_library(ABSOLUTE_PATH_AND_LOCAL NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)
find_library(ABSOLUTE_PATH_WITH_TYPE_AND_LOCAL NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)

find_library(NOTFOUND_PATH_AND_LOCAL NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)
find_library(NOTFOUND_PATH_WITH_TYPE_AND_LOCAL NAMES ${SEARCH_NAME} PATHS ${SEARCH_PATH} NO_DEFAULT_PATH)

message("RELATIVE_PATH_AND_LOCAL=${RELATIVE_PATH_AND_LOCAL}")
message("RELATIVE_PATH_WITH_TYPE_AND_LOCAL=${RELATIVE_PATH_WITH_TYPE_AND_LOCAL}")

message("ABSOLUTE_PATH_AND_LOCAL=${ABSOLUTE_PATH_AND_LOCAL}")
message("ABSOLUTE_PATH_WITH_TYPE_AND_LOCAL=${ABSOLUTE_PATH_WITH_TYPE_AND_LOCAL}")

message("NOTFOUND_PATH_AND_LOCAL=${NOTFOUND_PATH_AND_LOCAL}")
message("NOTFOUND_PATH_WITH_TYPE_AND_LOCAL=${NOTFOUND_PATH_WITH_TYPE_AND_LOCAL}")
