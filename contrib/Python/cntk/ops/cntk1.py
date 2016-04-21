# This file is auto-generated by _fetch_ops.py.

from cntk.graph import ComputationNode, InputComputationNodeBase, ImageInputComputationNodeBase


class Slice(ComputationNode):

    def __init__(self, beginIndex, endIndex, input, axis=1, name='Slice',
                 var_name=None):
        super(Slice, self).__init__(
            params=['value', 'format'], name=name, var_name=var_name)
        self.beginIndex = beginIndex
        self.endIndex = endIndex
        self.input = input
        self.axis = axis


class Splice(ComputationNode):

    def __init__(self, beginIndex, endIndex, input, axis=1, name='Splice',
                 var_name=None):
        super(Splice, self).__init__(
            params=['value', 'format'], name=name, var_name=var_name)
        self.beginIndex = beginIndex
        self.endIndex = endIndex
        self.input = input
        self.axis = axis


class ElementDivide(ComputationNode):

    def __init__(self, aMatrix, anotherMatrix, name='ElementDivide', var_name=None):
        super(ElementDivide, self).__init__(
            params=['aMatrix', 'anotherMatrix'], name=name, var_name=var_name)
        self.aMatrix = aMatrix
        self.anotherMatrix = anotherMatrix

class Ceil(ComputationNode):

    def __init__(self, x, name='Ceil', var_name=None):
        super(Ceil, self).__init__(params=['x'], name=name, var_name=var_name)
        self.x = x
        self.params_with_defaults = []


class Round(ComputationNode):

    def __init__(self, x, name='Round', var_name=None):
        super(Round, self).__init__(params=['x'], name=name, var_name=var_name)
        self.x = x
        self.params_with_defaults = []


class Sign(ComputationNode):

    def __init__(self, x, name='Sign', var_name=None):
        super(Sign, self).__init__(params=['x'], name=name, var_name=var_name)
        self.x = x
        self.params_with_defaults = []


class Min(ComputationNode):

    def __init__(self, a, b, name='Min', var_name=None):
        super(Min, self).__init__(
            params=['a', 'b'], name=name, var_name=var_name)
        self.a = a
        self.b = b
        self.params_with_defaults = []


class Max(ComputationNode):

    def __init__(self, a, b, name='Max', var_name=None):
        super(Max, self).__init__(
            params=['a', 'b'], name=name, var_name=var_name)
        self.a = a
        self.b = b
        self.params_with_defaults = []


class Fac(ComputationNode):

    def __init__(self, n, name='Fac', var_name=None):
        super(Fac, self).__init__(params=['n'], name=name, var_name=var_name)
        self.n = n
        self.params_with_defaults = []


class IsSameObject(ComputationNode):

    def __init__(self, a, b, name='IsSameObject', var_name=None):
        super(IsSameObject, self).__init__(
            params=['a', 'b'], name=name, var_name=var_name)
        self.a = a
        self.b = b
        self.params_with_defaults = []


class LearnableParameter(ComputationNode):

    def __init__(self, rows, cols, learningRateMultiplier=1.0, init='uniform', initValueScale=1, value=0, initFromFilePath='', initFromLiteral='', initOnCPUOnly=True, randomSeed=-1, name='LearnableParameter', var_name=None):
        super(LearnableParameter, self).__init__(params=['rows', 'cols', 'learningRateMultiplier', 'init', 'initValueScale',
                                                         'value', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed'], name=name, var_name=var_name)
        self.rows = rows
        self.cols = cols
        self.learningRateMultiplier = learningRateMultiplier
        self.init = init
        self.initValueScale = initValueScale
        self.value = value
        self.initFromFilePath = initFromFilePath
        self.initFromLiteral = initFromLiteral
        self.initOnCPUOnly = initOnCPUOnly
        self.randomSeed = randomSeed
        self.params_with_defaults = ['learningRateMultiplier', 'init', 'initValueScale',
                                     'value', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed']


class ParameterTensor(ComputationNode):

    def __init__(self, dims, learningRateMultiplier=1.0, init='uniform', initValueScale=1, value=0, initFromFilePath='', initFromLiteral='', initOnCPUOnly=True, randomSeed=-1, name='ParameterTensor', var_name=None):
        super(ParameterTensor, self).__init__(params=['dims', 'learningRateMultiplier', 'init', 'initValueScale',
                                                      'value', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed'], name=name, var_name=var_name)
        self.dims = dims
        self.learningRateMultiplier = learningRateMultiplier
        self.init = init
        self.initValueScale = initValueScale
        self.value = value
        self.initFromFilePath = initFromFilePath
        self.initFromLiteral = initFromLiteral
        self.initOnCPUOnly = initOnCPUOnly
        self.randomSeed = randomSeed
        self.params_with_defaults = ['learningRateMultiplier', 'init', 'initValueScale',
                                     'value', 'initFromFilePath', 'initFromLiteral', 'initOnCPUOnly', 'randomSeed']


class Input(InputComputationNodeBase):

    def __init__(self, dims, tag='feature', name='Input', var_name=None):
        super(Input, self).__init__(
            params=['dims', 'tag'], name=name, var_name=var_name)
        self.dims = dims
        self.tag = tag
        self.params_with_defaults = ['tag']


class SparseInput(InputComputationNodeBase):

    def __init__(self, dims, tag='feature', name='SparseInput', var_name=None):
        super(SparseInput, self).__init__(
            params=['dims', 'tag'], name=name, var_name=var_name)
        self.dims = dims
        self.tag = tag
        self.params_with_defaults = ['tag']


class ImageInput(ImageInputComputationNodeBase):

    def __init__(self, imageWidth, imageHeight, imageChannels, imageLayout='CHW', tag='feature', name='ImageInput', var_name=None):
        super(ImageInput, self).__init__(params=[
            'imageWidth', 'imageHeight', 'imageChannels', 'imageLayout', 'tag'], name=name, var_name=var_name)
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageChannels = imageChannels
        self.imageLayout = imageLayout
        self.tag = tag
        self.params_with_defaults = ['imageLayout', 'tag']


class SparseImageInput(ImageInputComputationNodeBase):

    def __init__(self, imageWidth, imageHeight, imageChannels, imageLayout='CHW', tag='feature', name='SparseImageInput', var_name=None):
        super(SparseImageInput, self).__init__(params=[
            'imageWidth', 'imageHeight', 'imageChannels', 'imageLayout', 'tag'], name=name, var_name=var_name)
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageChannels = imageChannels
        self.imageLayout = imageLayout
        self.tag = tag
        self.params_with_defaults = ['imageLayout', 'tag']


class EnvironmentInput(ComputationNode):

    def __init__(self, propertyName, name='EnvironmentInput', var_name=None):
        super(EnvironmentInput, self).__init__(
            params=['propertyName'], name=name, var_name=var_name)
        self.propertyName = propertyName
        self.params_with_defaults = []


class PastValue(ComputationNode):

    def __init__(self, dims, input, timeStep=1, defaultHiddenActivation=0.1, name='PastValue', var_name=None):
        super(PastValue, self).__init__(params=[
            'dims', 'input', 'timeStep', 'defaultHiddenActivation'], name=name, var_name=var_name)
        self.dims = dims
        self.input = input
        self.timeStep = timeStep
        self.defaultHiddenActivation = defaultHiddenActivation
        self.params_with_defaults = ['timeStep', 'defaultHiddenActivation']


class FutureValue(ComputationNode):

    def __init__(self, dims, input, timeStep=1, defaultHiddenActivation=0.1, name='FutureValue', var_name=None):
        super(FutureValue, self).__init__(params=[
            'dims', 'input', 'timeStep', 'defaultHiddenActivation'], name=name, var_name=var_name)
        self.dims = dims
        self.input = input
        self.timeStep = timeStep
        self.defaultHiddenActivation = defaultHiddenActivation
        self.params_with_defaults = ['timeStep', 'defaultHiddenActivation']


class Shift(ComputationNode):

    def __init__(self, input, fromOffset, boundaryValue, boundaryMode=-1, dim=-1, name='Shift', var_name=None):
        super(Shift, self).__init__(params=[
            'input', 'fromOffset', 'boundaryValue', 'boundaryMode', 'dim'], name=name, var_name=var_name)
        self.input = input
        self.fromOffset = fromOffset
        self.boundaryValue = boundaryValue
        self.boundaryMode = boundaryMode
        self.dim = dim
        self.params_with_defaults = ['boundaryMode', 'dim']


class RowRepeat(ComputationNode):

    def __init__(self, input, numRepeats, name='RowRepeat', var_name=None):
        super(RowRepeat, self).__init__(
            params=['input', 'numRepeats'], name=name, var_name=var_name)
        self.input = input
        self.numRepeats = numRepeats
        self.params_with_defaults = []


class RowStack(ComputationNode):

    def __init__(self, inputs, name='RowStack', var_name=None):
        super(RowStack, self).__init__(
            params=['inputs'], name=name, var_name=var_name)
        self.inputs = inputs
        self.params_with_defaults = []


class Reshape(ComputationNode):

    def __init__(self, input, numRows, imageWidth=0, imageHeight=0, imageChannels=0, name='Reshape', var_name=None):
        super(Reshape, self).__init__(params=[
            'input', 'numRows', 'imageWidth', 'imageHeight', 'imageChannels'], name=name, var_name=var_name)
        self.input = input
        self.numRows = numRows
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.imageChannels = imageChannels
        self.params_with_defaults = [
            'imageWidth', 'imageHeight', 'imageChannels']


class NewReshape(ComputationNode):

    def __init__(self, input, dims, beginAxis=0, endAxis=0, name='NewReshape', var_name=None):
        super(NewReshape, self).__init__(
            params=['input', 'dims', 'beginAxis', 'endAxis'], name=name, var_name=var_name)
        self.input = input
        self.dims = dims
        self.beginAxis = beginAxis
        self.endAxis = endAxis
        self.params_with_defaults = ['beginAxis', 'endAxis']


class TransposeDimensions(ComputationNode):

    def __init__(self, input, axis1, axis2, name='TransposeDimensions', var_name=None):
        super(TransposeDimensions, self).__init__(
            params=['input', 'axis1', 'axis2'], name=name, var_name=var_name)
        self.input = input
        self.axis1 = axis1
        self.axis2 = axis2
        self.params_with_defaults = []


class Times(ComputationNode):

    def __init__(self, A, B, outputRank=1, name='Times', var_name=None):
        super(Times, self).__init__(
            params=['A', 'B', 'outputRank'], name=name, var_name=var_name)
        self.A = A
        self.B = B
        self.outputRank = outputRank
        self.params_with_defaults = ['outputRank']


class Logistic(ComputationNode):

    def __init__(self, label, probability, name='Logistic', var_name=None):
        super(Logistic, self).__init__(
            params=['label', 'probability'], name=name, var_name=var_name)
        self.label = label
        self.probability = probability
        self.params_with_defaults = []


class WeightedLogistic(ComputationNode):

    def __init__(self, label, probability, instanceWeight, name='WeightedLogistic', var_name=None):
        super(WeightedLogistic, self).__init__(
            params=['label', 'probability', 'instanceWeight'], name=name, var_name=var_name)
        self.label = label
        self.probability = probability
        self.instanceWeight = instanceWeight
        self.params_with_defaults = []


class ReconcileMBLayout(ComputationNode):

    def __init__(self, dataInput, layoutInput, name='ReconcileMBLayout', var_name=None):
        super(ReconcileMBLayout, self).__init__(
            params=['dataInput', 'layoutInput'], name=name, var_name=var_name)
        self.dataInput = dataInput
        self.layoutInput = layoutInput
        self.params_with_defaults = []


class Convolution(ComputationNode):

    def __init__(self, weightNode, inputValueNode, kernelDims, mapDims=1, stride=1, sharing=True, autoPadding=True, lowerPad=0, upperPad=0, imageLayout='CHW', maxTempMemSizeInSamples=0, name='Convolution', var_name=None):
        super(Convolution, self).__init__(params=['weightNode', 'inputValueNode', 'kernelDims', 'mapDims', 'stride', 'sharing',
                                                  'autoPadding', 'lowerPad', 'upperPad', 'imageLayout', 'maxTempMemSizeInSamples'], name=name, var_name=var_name)
        self.weightNode = weightNode
        self.inputValueNode = inputValueNode
        self.kernelDims = kernelDims
        self.mapDims = mapDims
        self.stride = stride
        self.sharing = sharing
        self.autoPadding = autoPadding
        self.lowerPad = lowerPad
        self.upperPad = upperPad
        self.imageLayout = imageLayout
        self.maxTempMemSizeInSamples = maxTempMemSizeInSamples
        self.params_with_defaults = ['mapDims', 'stride', 'sharing', 'autoPadding',
                                     'lowerPad', 'upperPad', 'imageLayout', 'maxTempMemSizeInSamples']


class Pooling(ComputationNode):

    def __init__(self, input, poolKind, kernelDims, stride=1, autoPadding=True, lowerPad=0, upperPad=0, imageLayout='CHW', name='Pooling', var_name=None):
        super(Pooling, self).__init__(params=['input', 'poolKind', 'kernelDims', 'stride',
                                              'autoPadding', 'lowerPad', 'upperPad', 'imageLayout'], name=name, var_name=var_name)
        self.input = input
        self.poolKind = poolKind
        self.kernelDims = kernelDims
        self.stride = stride
        self.autoPadding = autoPadding
        self.lowerPad = lowerPad
        self.upperPad = upperPad
        self.imageLayout = imageLayout
        self.params_with_defaults = [
            'stride', 'autoPadding', 'lowerPad', 'upperPad', 'imageLayout']


class MaxPooling(ComputationNode):

    def __init__(self, input, windowWidth, windowHeight, horizontalSubsample, verticalSubsample, imageLayout='CHW', name='MaxPooling', var_name=None):
        super(MaxPooling, self).__init__(params=[
            'input', 'windowWidth', 'windowHeight', 'horizontalSubsample', 'verticalSubsample', 'imageLayout'], name=name, var_name=var_name)
        self.input = input
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.horizontalSubsample = horizontalSubsample
        self.verticalSubsample = verticalSubsample
        self.imageLayout = imageLayout
        self.params_with_defaults = ['imageLayout']


class AveragePooling(ComputationNode):

    def __init__(self, input, windowWidth, windowHeight, horizontalSubsample, verticalSubsample, imageLayout='CHW', name='AveragePooling', var_name=None):
        super(AveragePooling, self).__init__(params=[
            'input', 'windowWidth', 'windowHeight', 'horizontalSubsample', 'verticalSubsample', 'imageLayout'], name=name, var_name=var_name)
        self.input = input
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.horizontalSubsample = horizontalSubsample
        self.verticalSubsample = verticalSubsample
        self.imageLayout = imageLayout
        self.params_with_defaults = ['imageLayout']


class BatchNormalization(ComputationNode):

    def __init__(self, input, scale, bias, runMean, runInvStdDev, spatial, normalizationTimeConstant=0, blendTimeConstant=0, epsilon=1e-05, useCntkEngine=True, imageLayout='CHW', name='BatchNormalization', var_name=None):
        super(BatchNormalization, self).__init__(params=['input', 'scale', 'bias', 'runMean', 'runInvStdDev', 'spatial',
                                                         'normalizationTimeConstant', 'blendTimeConstant', 'epsilon', 'useCntkEngine', 'imageLayout'], name=name, var_name=var_name)
        self.input = input
        self.scale = scale
        self.bias = bias
        self.runMean = runMean
        self.runInvStdDev = runInvStdDev
        self.spatial = spatial
        self.normalizationTimeConstant = normalizationTimeConstant
        self.blendTimeConstant = blendTimeConstant
        self.epsilon = epsilon
        self.useCntkEngine = useCntkEngine
        self.imageLayout = imageLayout
        self.params_with_defaults = [
            'normalizationTimeConstant', 'blendTimeConstant', 'epsilon', 'useCntkEngine', 'imageLayout']


class Abs(ComputationNode):

    def __init__(self, x, name='Abs', var_name=None):
        super(Abs, self).__init__(params=['x'], name=name, var_name=var_name)
        self.x = x
        self.params_with_defaults = []


class ClassBasedCrossEntropyWithSoftmax(ComputationNode):

    def __init__(self, labelClassDescriptorVectorSequence, mainInputInfo, mainWeight, classLogProbsBeforeSoftmax, name='ClassBasedCrossEntropyWithSoftmax', var_name=None):
        super(ClassBasedCrossEntropyWithSoftmax, self).__init__(params=[
            'labelClassDescriptorVectorSequence', 'mainInputInfo', 'mainWeight', 'classLogProbsBeforeSoftmax'], name=name, var_name=var_name)
        self.labelClassDescriptorVectorSequence = labelClassDescriptorVectorSequence
        self.mainInputInfo = mainInputInfo
        self.mainWeight = mainWeight
        self.classLogProbsBeforeSoftmax = classLogProbsBeforeSoftmax
        self.params_with_defaults = []


class ColumnElementTimes(ComputationNode):

    def __init__(self, aVectorSequence, anotherVectorSequence, name='ColumnElementTimes', var_name=None):
        super(ColumnElementTimes, self).__init__(
            params=['aVectorSequence', 'anotherVectorSequence'], name=name, var_name=var_name)
        self.aVectorSequence = aVectorSequence
        self.anotherVectorSequence = anotherVectorSequence
        self.params_with_defaults = []


class CosDistance(ComputationNode):

    def __init__(self, aVectorSequence, anotherVectorSequence, name='CosDistance', var_name=None):
        super(CosDistance, self).__init__(
            params=['aVectorSequence', 'anotherVectorSequence'], name=name, var_name=var_name)
        self.aVectorSequence = aVectorSequence
        self.anotherVectorSequence = anotherVectorSequence
        self.params_with_defaults = []


class CosDistanceWithNegativeSamples(ComputationNode):

    def __init__(self, aVectorSequence, anotherVectorSequence, numShifts, numNegSamples, name='CosDistanceWithNegativeSamples', var_name=None):
        super(CosDistanceWithNegativeSamples, self).__init__(params=[
            'aVectorSequence', 'anotherVectorSequence', 'numShifts', 'numNegSamples'], name=name, var_name=var_name)
        self.aVectorSequence = aVectorSequence
        self.anotherVectorSequence = anotherVectorSequence
        self.numShifts = numShifts
        self.numNegSamples = numNegSamples
        self.params_with_defaults = []


class Cosine(ComputationNode):

    def __init__(self, x, name='Cosine', var_name=None):
        super(Cosine, self).__init__(
            params=['x'], name=name, var_name=var_name)
        self.x = x
        self.params_with_defaults = []


class CrossEntropy(ComputationNode):

    def __init__(self, refProbVectorSequence, outProbVectorSequence, name='CrossEntropy', var_name=None):
        super(CrossEntropy, self).__init__(params=[
            'refProbVectorSequence', 'outProbVectorSequence'], name=name, var_name=var_name)
        self.refProbVectorSequence = refProbVectorSequence
        self.outProbVectorSequence = outProbVectorSequence
        self.params_with_defaults = []


class CrossEntropyWithSoftmax(ComputationNode):

    def __init__(self, labelVectorSequence, outProbVectorSequence, name='CrossEntropyWithSoftmax', var_name=None):
        super(CrossEntropyWithSoftmax, self).__init__(params=[
            'labelVectorSequence', 'outProbVectorSequence'], name=name, var_name=var_name)
        self.labelVectorSequence = labelVectorSequence
        self.outProbVectorSequence = outProbVectorSequence
        self.params_with_defaults = []


class DiagTimes(ComputationNode):

    def __init__(self, diagonalMatrixAsColumnVector, matrix, name='DiagTimes', var_name=None):
        super(DiagTimes, self).__init__(
            params=['diagonalMatrixAsColumnVector', 'matrix'], name=name, var_name=var_name)
        self.diagonalMatrixAsColumnVector = diagonalMatrixAsColumnVector
        self.matrix = matrix
        self.params_with_defaults = []


class Dropout(ComputationNode):

    def __init__(self, activationVectorSequence, name='Dropout', var_name=None):
        super(Dropout, self).__init__(
            params=['activationVectorSequence'], name=name, var_name=var_name)
        self.activationVectorSequence = activationVectorSequence
        self.params_with_defaults = []


class ElementTimes(ComputationNode):

    def __init__(self, aMatrix, anotherMatrix, name='ElementTimes', var_name=None):
        super(ElementTimes, self).__init__(
            params=['aMatrix', 'anotherMatrix'], name=name, var_name=var_name)
        self.aMatrix = aMatrix
        self.anotherMatrix = anotherMatrix
        self.params_with_defaults = []


class ErrorPrediction(ComputationNode):

    def __init__(self, labelVectorSequence, outVectorSequence, name='ErrorPrediction', var_name=None):
        super(ErrorPrediction, self).__init__(
            params=['labelVectorSequence', 'outVectorSequence'], name=name, var_name=var_name)
        self.labelVectorSequence = labelVectorSequence
        self.outVectorSequence = outVectorSequence
        self.params_with_defaults = []


class Exp(ComputationNode):

    def __init__(self, x, name='Exp', var_name=None):
        super(Exp, self).__init__(params=['x'], name=name, var_name=var_name)
        self.x = x
        self.params_with_defaults = []


class GatherPacked(ComputationNode):

    def __init__(self, indexSequence, sourceData, name='GatherPacked', var_name=None):
        super(GatherPacked, self).__init__(
            params=['indexSequence', 'sourceData'], name=name, var_name=var_name)
        self.indexSequence = indexSequence
        self.sourceData = sourceData
        self.params_with_defaults = []


class GMMLogLikelihood(ComputationNode):

    def __init__(self, unnormalizedPriorVector, meansAsRows, logStdDevAsRows, dataVectorSequence, name='GMMLogLikelihood', var_name=None):
        super(GMMLogLikelihood, self).__init__(params=[
            'unnormalizedPriorVector', 'meansAsRows', 'logStdDevAsRows', 'dataVectorSequence'], name=name, var_name=var_name)
        self.unnormalizedPriorVector = unnormalizedPriorVector
        self.meansAsRows = meansAsRows
        self.logStdDevAsRows = logStdDevAsRows
        self.dataVectorSequence = dataVectorSequence
        self.params_with_defaults = []


class If(ComputationNode):
    def __init__(self, cond, thenVal, elseVal, name='BS.Boolean.If', var_name=None):
        super(If, self).__init__(
            params=['cond', 'thenVal', 'elseVal'], name=name, var_name=var_name)
        self.cond = cond
        self.thenVal = thenVal
        self.elseVal = elseVal
        self.params_with_defaults = []


class InvStdDev(ComputationNode):

    def __init__(self, dataVectorSequence, name='InvStdDev', var_name=None):
        super(InvStdDev, self).__init__(
            params=['dataVectorSequence'], name=name, var_name=var_name)
        self.dataVectorSequence = dataVectorSequence
        self.params_with_defaults = []


class KhatriRaoProduct(ComputationNode):

    def __init__(self, leftMatrix, rightMatrix, name='KhatriRaoProduct', var_name=None):
        super(KhatriRaoProduct, self).__init__(
            params=['leftMatrix', 'rightMatrix'], name=name, var_name=var_name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix
        self.params_with_defaults = []


class Log(ComputationNode):

    def __init__(self, x, name='Log', var_name=None):
        super(Log, self).__init__(params=['x'], name=name, var_name=var_name)
        self.x = x
        self.params_with_defaults = []


class LogSoftmax(ComputationNode):

    def __init__(self, z, name='LogSoftmax', var_name=None):
        super(LogSoftmax, self).__init__(
            params=['z'], name=name, var_name=var_name)
        self.z = z
        self.params_with_defaults = []


class MatrixL1Reg(ComputationNode):

    def __init__(self, matrix, name='MatrixL1Reg', var_name=None):
        super(MatrixL1Reg, self).__init__(
            params=['matrix'], name=name, var_name=var_name)
        self.matrix = matrix
        self.params_with_defaults = []


class MatrixL2Reg(ComputationNode):

    def __init__(self, matrix, name='MatrixL2Reg', var_name=None):
        super(MatrixL2Reg, self).__init__(
            params=['matrix'], name=name, var_name=var_name)
        self.matrix = matrix
        self.params_with_defaults = []


class Mean(ComputationNode):

    def __init__(self, dataVectorSequence, name='Mean', var_name=None):
        super(Mean, self).__init__(
            params=['dataVectorSequence'], name=name, var_name=var_name)
        self.dataVectorSequence = dataVectorSequence
        self.params_with_defaults = []


class Minus(ComputationNode):

    def __init__(self, leftMatrix, rightMatrix, name='Minus', var_name=None):
        super(Minus, self).__init__(
            params=['leftMatrix', 'rightMatrix'], name=name, var_name=var_name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix
        self.params_with_defaults = []


class Negate(ComputationNode):

    def __init__(self, input, name='Negate', var_name=None):
        super(Negate, self).__init__(
            params=['input'], name=name, var_name=var_name)
        self.input = input
        self.params_with_defaults = []


class PackedIndex(ComputationNode):

    def __init__(self, targetObject, indexSequence, name='PackedIndex', var_name=None):
        super(PackedIndex, self).__init__(
            params=['targetObject', 'indexSequence'], name=name, var_name=var_name)
        self.targetObject = targetObject
        self.indexSequence = indexSequence
        self.params_with_defaults = []


class Pass(ComputationNode):

    def __init__(self, x, name='Pass', var_name=None):
        super(Pass, self).__init__(params=['x'], name=name, var_name=var_name)
        self.x = x
        self.params_with_defaults = []


class PerDimMeanVarDeNormalization(ComputationNode):

    def __init__(self, dataVectorSequence, meanVector, invStdDevVector, name='PerDimMeanVarDeNormalization', var_name=None):
        super(PerDimMeanVarDeNormalization, self).__init__(params=[
            'dataVectorSequence', 'meanVector', 'invStdDevVector'], name=name, var_name=var_name)
        self.dataVectorSequence = dataVectorSequence
        self.meanVector = meanVector
        self.invStdDevVector = invStdDevVector
        self.params_with_defaults = []


class PerDimMeanVarNormalization(ComputationNode):

    def __init__(self, dataVectorSequence, meanVector, invStdDevVector, name='PerDimMeanVarNormalization', var_name=None):
        super(PerDimMeanVarNormalization, self).__init__(params=[
            'dataVectorSequence', 'meanVector', 'invStdDevVector'], name=name, var_name=var_name)
        self.dataVectorSequence = dataVectorSequence
        self.meanVector = meanVector
        self.invStdDevVector = invStdDevVector
        self.params_with_defaults = []


class Plus(ComputationNode):

    def __init__(self, leftMatrix, rightMatrix, name='Plus', var_name=None):
        super(Plus, self).__init__(
            params=['leftMatrix', 'rightMatrix'], name=name, var_name=var_name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix
        self.params_with_defaults = []


class Reciprocal(ComputationNode):

    def __init__(self, z, name='Reciprocal', var_name=None):
        super(Reciprocal, self).__init__(
            params=['z'], name=name, var_name=var_name)
        self.z = z
        self.params_with_defaults = []


class RectifiedLinear(ComputationNode):

    def __init__(self, z, name='RectifiedLinear', var_name=None):
        super(RectifiedLinear, self).__init__(
            params=['z'], name=name, var_name=var_name)
        self.z = z
        self.params_with_defaults = []


class Scale(ComputationNode):

    def __init__(self, scalarScalingFactor, matrix, name='Scale', var_name=None):
        super(Scale, self).__init__(
            params=['scalarScalingFactor', 'matrix'], name=name, var_name=var_name)
        self.scalarScalingFactor = scalarScalingFactor
        self.matrix = matrix
        self.params_with_defaults = []


class ScatterPacked(ComputationNode):

    def __init__(self, cond, indexSequence, sourceData, name='ScatterPacked', var_name=None):
        super(ScatterPacked, self).__init__(
            params=['cond', 'indexSequence', 'sourceData'], name=name, var_name=var_name)
        self.cond = cond
        self.indexSequence = indexSequence
        self.sourceData = sourceData
        self.params_with_defaults = []


class Sigmoid(ComputationNode):

    def __init__(self, z, name='Sigmoid', var_name=None):
        super(Sigmoid, self).__init__(
            params=['z'], name=name, var_name=var_name)
        self.z = z
        self.params_with_defaults = []


class Softmax(ComputationNode):

    def __init__(self, z, name='Softmax', var_name=None):
        super(Softmax, self).__init__(
            params=['z'], name=name, var_name=var_name)
        self.z = z
        self.params_with_defaults = []


class Hardmax(ComputationNode):

    def __init__(self, z, name='Hardmax', var_name=None):
        super(Hardmax, self).__init__(
            params=['z'], name=name, var_name=var_name)
        self.z = z
        self.params_with_defaults = []


class Sqrt(ComputationNode):

    def __init__(self, z, name='Sqrt', var_name=None):
        super(Sqrt, self).__init__(params=['z'], name=name, var_name=var_name)
        self.z = z
        self.params_with_defaults = []


class SquareError(ComputationNode):

    def __init__(self, aMatrix, anotherMatrix, name='SquareError', var_name=None):
        super(SquareError, self).__init__(
            params=['aMatrix', 'anotherMatrix'], name=name, var_name=var_name)
        self.aMatrix = aMatrix
        self.anotherMatrix = anotherMatrix
        self.params_with_defaults = []


class SumColumnElements(ComputationNode):

    def __init__(self, z, name='SumColumnElements', var_name=None):
        super(SumColumnElements, self).__init__(
            params=['z'], name=name, var_name=var_name)
        self.z = z
        self.params_with_defaults = []


class SumElements(ComputationNode):

    def __init__(self, matrix, name='SumElements', var_name=None):
        super(SumElements, self).__init__(
            params=['matrix'], name=name, var_name=var_name)
        self.matrix = matrix
        self.params_with_defaults = []


class Tanh(ComputationNode):

    def __init__(self, z, name='Tanh', var_name=None):
        super(Tanh, self).__init__(params=['z'], name=name, var_name=var_name)
        self.z = z
        self.params_with_defaults = []


class TimeReverse(ComputationNode):

    def __init__(self, vectorSequence, name='TimeReverse', var_name=None):
        super(TimeReverse, self).__init__(
            params=['vectorSequence'], name=name, var_name=var_name)
        self.vectorSequence = vectorSequence
        self.params_with_defaults = []


class TransposeTimes(ComputationNode):

    def __init__(self, leftMatrix, rightMatrix, name='TransposeTimes', var_name=None):
        super(TransposeTimes, self).__init__(
            params=['leftMatrix', 'rightMatrix'], name=name, var_name=var_name)
        self.leftMatrix = leftMatrix
        self.rightMatrix = rightMatrix
        self.params_with_defaults = []


class Where(ComputationNode):

    def __init__(self, cond, name='Where', var_name=None):
        super(Where, self).__init__(
            params=['cond'], name=name, var_name=var_name)
        self.cond = cond
        self.params_with_defaults = []

Parameter = LearnableParameter
ColumnwiseCrossProduct = KhatriRaoProduct
ClassificationError = ErrorPrediction
Delay = PastValue


class ConstantTensor(ParameterTensor):

    def __init__(self, value, dims, name='ConstantTensor', var_name=None):
        super(ConstantTensor, self).__init__(dims, learningRateMultiplier=0,
                                             init='fixedValue', value=value, name=name, var_name=var_name)
        self.params = ['value', 'dims']
        self.params_with_defaults = []


class Constant(Parameter):

    def __init__(self, value, rows=1, cols=1, name='Constant', var_name=None):
        super(Constant, self).__init__(rows, cols, learningRateMultiplier=0,
                                       init='fixedValue', value=value, name=name, var_name=var_name)
        self.params = ['value', 'rows', 'cols']
        self.params_with_defaults = ['rows', 'cols']


class RowSlice(Slice):

    def __init__(self, beginIndex, numRows, input, name='RowSlice', var_name=None):
        super(RowSlice, self).__init__(
            beginIndex, beginIndex + numRows, input, axis=1, name=name, var_name=var_name)
        self.params = ['beginIndex', 'numRows', 'input']
        self.params_with_defaults = []


class ReshapeDimension(NewReshape):

    def __init__(self, x, axis, tensorShape, name='ReshapeDimension', var_name=None):
        super(ReshapeDimension, self).__init__(
            x, tensorShape, beginAxis=axis, endAxis=axis + 1, name=name, var_name=var_name)
        self.params = ['x', 'axis', 'tensorShape']
        self.params_with_defaults = []


class FlattenDimensions(NewReshape):

    def __init__(self, x, axis, num, name='FlattenDimensions', var_name=None):
        super(FlattenDimensions, self).__init__(
            x, 0, beginAxis=axis, endAxis=axis + num, name=name, var_name=var_name)
        self.params = ['x', 'axis', 'num']
        self.params_with_defaults = []


class SplitDimension(ReshapeDimension):

    def __init__(self, x, axis, N, name='SplitDimension', var_name=None):
        super(SplitDimension, self).__init__(
            x, axis, '<not yet supported>', name=name, var_name=var_name)
        self.params = ['x', 'axis', 'N']
        self.params_with_defaults = []


class Transpose(TransposeDimensions):

    def __init__(self, x, name='Transpose', var_name=None):
        super(Transpose, self).__init__(x, 1, 2, name=name, var_name=var_name)
        self.params = ['x']
        self.params_with_defaults = []
