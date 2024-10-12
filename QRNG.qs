open Microsoft.Quantum.Convert;
open Microsoft.Quantum.Intrinsic;
open Microsoft.Quantum.Math;

operation GenerateRandomNumberInRange(max : Int) : Int {
    mutable bits = [];
    let nBits = BitSizeI(max);
    for idxBit in 1..nBits {
        set bits += [GenerateRandomBit()];
    }
    let sample = ResultArrayAsInt(bits);

    return sample > max ? GenerateRandomNumberInRange(max) | sample;
}

operation GenerateRandomBit() : Result {
    use q = Qubit();
    H(q);
    let result = M(q);
    Reset(q);
    return result;
}

@EntryPoint()
operation Main() : Result {
    let randomNumber = GenerateRandomNumberInRange(100000);
    Message($"Random number: {randomNumber}");
    return Zero;
}