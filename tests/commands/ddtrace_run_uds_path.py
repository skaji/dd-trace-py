from ddtrace import tracer

if __name__ == '__main__':
    assert tracer.uds_path is not None
    print('Test success')
